import json
from rest_framework.renderers import JSONRenderer

class PrettyJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            return super().render(data, accepted_media_type, renderer_context)

        # Форматирование с отступами
        return json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8')
