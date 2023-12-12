# Generated by Django 4.2.6 on 2023-12-12 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('actor_name', models.CharField(max_length=255)),
                ('profile_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('character_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('imdb_id', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('poster_path', models.CharField(max_length=255)),
                ('background_path', models.CharField(max_length=255)),
                ('original_language', models.CharField(max_length=20)),
                ('original_title', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('release_date', models.IntegerField()),
                ('runtime', models.FloatField()),
                ('vote_average', models.FloatField(max_length=255)),
                ('vote_count', models.IntegerField()),
                ('popularity', models.FloatField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('is_public', models.BooleanField(default=True, null=True)),
                ('upvotes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('downvotes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('total_time_of_movies', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('movies', models.ManyToManyField(blank=True, related_name='lists', to='APImovie.movie')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-upvotes'],
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rate_point', models.FloatField(blank=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APImovie.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APImovie.crew')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APImovie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APImovie.genre')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APImovie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='APImovie.movie')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='APImovie.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APImovie.actor')),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APImovie.character')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APImovie.movie')),
            ],
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
