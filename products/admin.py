from django.contrib import admin

from products.models import (
    ProductModel
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


admin.site.register(ProductModel, ProductAdmin)
