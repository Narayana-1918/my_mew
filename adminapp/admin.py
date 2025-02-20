from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# Register your models here.
@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','price','photo']