# Generated by Django 3.0 on 2019-12-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameViewer', '0002_game_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='picture',
            field=models.ImageField(blank=True, upload_to='game_cover_art/'),
        ),
    ]