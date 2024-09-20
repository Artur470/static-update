from rest_framework import serializers
from .models import Cart, CartItem, Order, PaymentMethod
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemsSerializer(serializers.ModelSerializer):
    cart_id = serializers.IntegerField(source='cart.id', read_only=True)
    product_id = serializers.IntegerField(source='product.id', read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        cart = validated_data.get('cart')
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        user = self.context['request'].user

        if product.quantity < quantity:
            raise serializers.ValidationError('Not enough stock available.')

        # Устанавливаем цену с учетом промо-цены
        price = product.promotion if product.promotion is not None else product.price
        total_price = price * quantity

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity, 'price': total_price, 'user': user}
        )

        if not created:
            # Если элемент уже существует, увеличиваем количество и пересчитываем цену
            if product.quantity < quantity:
                raise serializers.ValidationError('Not enough stock available.')

            # Обновляем количество и цену
            product.quantity -= (quantity - cart_item.quantity)
            cart_item.quantity = quantity
            cart_item.price = price * quantity
            product.save()
            cart_item.save()
        else:
            # Если элемент создан, уменьшаем количество товара на складе
            product.quantity -= quantity
            product.save()

        # Пересчитываем общую стоимость корзины
        cart.total_price = sum(item.price for item in CartItem.objects.filter(cart=cart))
        cart.save()

        return cart_item

    def update(self, instance, validated_data):
        new_quantity = validated_data.get('quantity', instance.quantity)
        product = instance.product

        if new_quantity != instance.quantity:
            if product.quantity + instance.quantity < new_quantity:
                raise serializers.ValidationError('Not enough stock available.')

            # Обновляем количество товара на складе
            product.quantity += instance.quantity - new_quantity

            # Устанавливаем цену с учетом промо-цены
            price = product.promotion if product.promotion is not None else product.price
            instance.price = price * new_quantity

            instance.quantity = new_quantity
            product.save()
            instance.save()

            # Пересчитываем общую стоимость корзины
            cart = instance.cart
            cart.total_price = sum(item.price for item in CartItem.objects.filter(cart=cart))
            cart.save()

        return instance


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'name']


class OrderSerializer(serializers.ModelSerializer):
    payment_method = serializers.PrimaryKeyRelatedField(queryset=PaymentMethod.objects.all())

    class Meta:
        model = Order
        fields = ['user', 'cart', 'total_price', 'address', 'payment_method']
