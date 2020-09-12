from django.contrib import admin
from products.models import Products

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name","price","productCode"]
    class Meta:
        model=Products
