# Generated by Django 5.0.3 on 2024-06-13 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_featuredproducts_description_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categories',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='featuredproducts',
            table='featuredproducts',
        ),
        migrations.AlterModelTable(
            name='products',
            table='products',
        ),
    ]
