# Generated by Django 4.2.6 on 2023-11-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APImovie', '0003_movielist'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default=None, null=True, unique=True),
        ),
    ]
