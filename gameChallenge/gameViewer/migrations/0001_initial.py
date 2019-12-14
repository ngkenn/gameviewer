# Generated by Django 3.0 on 2019-12-14 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('publisher', models.CharField(max_length=50)),
                ('n_players', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Games',
            },
        ),
    ]