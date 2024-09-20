from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils import timezone
import pytz

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.total_price)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)  # Хранит актуальную цену (с учетом промо, если она есть)
    isOrder = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.product.promotion is not None:
            self.price = self.product.promotion * self.quantity
        else:
            self.price = self.product.price * self.quantity
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} {self.product.title}"



# @receiver(pre_save, sender=CartItem)
# def correct_price(sender, instance, **kwargs):
#     product = instance.product
#     quantity = instance.quantity
#     price_of_product = float(product.price)
#
#     if instance.promotion is not None and instance.promotion > 0:
#         # Применяем скидку, если она существует и больше нуля
#         discount_percentage = instance.promotion
#         discounted_price = price_of_product * (1 - discount_percentage / 100)
#         instance.price = quantity * discounted_price
#     else:
#         # Без промоакции
#         instance.price = quantity * price_of_product


#order

class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)  # Например: "Card", "Cash", "Bank Transfer"
    description = models.TextField(blank=True, null=True)  # Дополнительное описание (по желанию)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, null=True, blank=True, on_delete=models.SET_NULL)
    total_price = models.FloatField()
    address = models.CharField(max_length=255)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"

    def clear_user_cart(self):
        # Очистите корзину пользователя
        self.cart.cartitem_set.all().delete()
        self.cart.total_price = 0
        self.cart.save()

    def send_order_email(self):
        order_time_utc = self.ordered_at  # или datetime.utcnow().replace(tzinfo=pytz.utc)
        timezone = pytz.timezone('Asia/Bishkek')
        order_time_local = order_time_utc.astimezone(timezone)
        order_time_str = order_time_local.strftime('%Y-%m-%d %H:%M:%S')

        subject = 'Новый заказ!'
        message = f'Номер заказа: {self.id}\n' \
                  f'Email Пользователя: {self.user.email}\n' \
                  f'Имя пользователя: {self.user.first_name}, {self.user.last_name}\n' \
                  f'Номер телефона пользователя: {self.user.number}\n' \
                  f'Адрес: {self.address}\n' \
                  f'Способ оплаты: {self.payment_method.name if self.payment_method else "Не указан"}\n' \
                  f'Окончательная цена: {self.total_price}\n' \
                  f'Время заказа: {order_time_str}\n\n'

        if self.user.wholesaler:
            message += "Покупатель является оптовиком.\n\n"

        items = self.cart.cartitem_set.all()
        if items.exists():
            message += "\nТовары в заказе:\n\n"
            for item in items:
                message += f'ID продукта: {item.product.id}\n' \
                           f'Продукт: {item.product.title}\n' \
                           f'Категория: {item.product.category}\n' \
                           f'Цвет: {item.product.color}\n' \
                           f'Бренд: {item.product.brand}\n' \
                           f'Количество: {item.quantity}\n' \
                           f'Цена за 1 товар: {item.price / item.quantity}\n' \
                           f'Цена за все товары: {item.price}\n\n' \

        admin_email = 'homelife.site.kg@gmail.com'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])
