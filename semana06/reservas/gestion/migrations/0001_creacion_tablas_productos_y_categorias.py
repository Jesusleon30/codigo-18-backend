# Generated by Django 5.0.6 on 2024-06-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='caterogiaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updatedAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='ProductoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('disponible', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
            ],
        ),
    ]
