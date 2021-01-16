from django.db import models


class Product(models.Model):
    price = models.FloatField()
    image = models.ImageField()
    description = models.TextField()
    assessment = models.IntegerField()
    name = models.CharField(max_length=1000)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
