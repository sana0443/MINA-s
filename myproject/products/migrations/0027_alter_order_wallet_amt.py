# Generated by Django 4.1.5 on 2023-03-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_order_wallet_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='wallet_amt',
            field=models.FloatField(default=0),
        ),
    ]
