from django.db import models


class ClientModel(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True)
    email = models.EmailField()

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
