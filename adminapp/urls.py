from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
app_name='adminapp'
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('view/',view,name='view'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)