from django.contrib import admin

from categories.models import (
    CategoryModel
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(CategoryModel, CategoryAdmin)
