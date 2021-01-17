from django.contrib import admin

from products.models import (
    Product
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'category',
                'price',
                'assessment',
                'image',
                'description',
            )
        }),
    )


admin.site.register(Product, ProductAdmin)
