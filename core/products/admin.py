from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "photo",
        "manufacturer",
        "seller",
        "status",
    )


admin.site.register(Product, ProductAdmin)
