# Generated by Django 5.0.4 on 2024-05-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
