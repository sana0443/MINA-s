# Generated by Django 4.1.5 on 2023-03-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_remove_order_phone_address_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
