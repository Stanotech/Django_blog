# Generated by Django 3.2.12 on 2022-12-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20221122_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
