# Generated by Django 4.1.5 on 2023-03-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order confirmed', 'Order confirmed'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Order confirmed', max_length=50),
        ),
    ]
