from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=25)
    price=models.FloatField()
    photo=models.ImageField()