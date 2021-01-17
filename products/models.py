from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    image = models.ImageField()
    description = models.TextField()
    name = models.CharField(max_length=1000)
    price = models.FloatField(validators=[MinValueValidator(0)])
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    assessment = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
