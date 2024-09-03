from django.apps import AppConfig


class ShopAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shop_app"
    verbose_name = "Shop App"

    def ready(self):
        from . import signals

        # print("Inited signals:", signals, "for", self.name)
