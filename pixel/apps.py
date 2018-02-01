from django.apps import AppConfig


class PixelConfig(AppConfig):
    name = 'pixel'

    def ready(self):
        from pixel import signals  # noqa
