# Generated by Django 4.2.6 on 2023-11-30 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APImovie', '0005_alter_genre_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movielist',
            options={'ordering': ['-upvotes']},
        ),
        migrations.AlterField(
            model_name='movielist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_upvote', models.BooleanField()),
                ('movie_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='APImovie.movielist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'movie_list')},
            },
        ),
    ]
