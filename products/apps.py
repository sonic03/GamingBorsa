from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'


    def ready(self):
        from apiandupdate import updater
        updater.start()
