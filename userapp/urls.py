from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
app_name='userapp'
urlpatterns = [
    path('register/',register,name='register'),
    path('view/',view,name='view'),
    path('products/',products,name='products'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete_data,name='delete'),



]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)