# Generated by Django 4.1.5 on 2023-03-17 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_alter_orderitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]