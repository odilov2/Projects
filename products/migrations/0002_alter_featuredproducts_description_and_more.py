# Generated by Django 5.0.3 on 2024-03-30 02:51

import mdeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredproducts',
            name='description',
            field=mdeditor.fields.MDTextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
