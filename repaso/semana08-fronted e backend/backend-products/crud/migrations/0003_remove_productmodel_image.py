# Generated by Django 5.0.7 on 2024-07-21 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_productmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='image',
        ),
    ]
