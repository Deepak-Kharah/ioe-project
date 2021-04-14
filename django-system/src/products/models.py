from django.db import models


class Product(models.Model):
    image = models.ImageField(name='Model image', null=True, blank=True)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(name='price', null=True, blank=True)
    description = models.TextField(name='description', null=True, blank=True)

    def __str__(self):
        return self.product_name
