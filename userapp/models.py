from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    age=models.IntegerField()
    photo=models.ImageField(upload_to='media/')
