# Generated by Django 4.1.5 on 2023-02-20 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='otp',
            field=models.IntegerField(),
        ),
    ]
