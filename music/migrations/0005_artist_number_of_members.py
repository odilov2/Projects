# Generated by Django 5.0.3 on 2024-05-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_songs_music_songs_id_8977f4_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='number_of_members',
            field=models.IntegerField(default=0),
        ),
    ]
