from django.contrib import admin

from clients.models import (
    ClientModel,
)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    fieldsets = (
        (None, {
            'fields': ('email',)
        }),
    )


admin.site.register(ClientModel, ClientAdmin)