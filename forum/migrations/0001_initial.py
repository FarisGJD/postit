# Generated by Django 3.2.13 on 2022-05-18 22:08

import cloudinary.models
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
            name='Postit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_starter', models.BooleanField(default=True)),
                ('heading', models.CharField(max_length=300, unique=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('generated_on', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('topic', models.CharField(max_length=20, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_posts', to=settings.AUTH_USER_MODEL)),
                ('votes', models.ManyToManyField(blank=True, related_name='post_votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-generated_on'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('postit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_comments', to='forum.postit')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reply', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('postit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.postit')),
                ('replies', models.ManyToManyField(blank=True, to='forum.Reply')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ManyToManyField(blank=True, related_name='user_categories', to='forum.Postit')),
            ],
        ),
    ]