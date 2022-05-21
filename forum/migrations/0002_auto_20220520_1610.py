# Generated by Django 3.2.13 on 2022-05-20 16:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=300, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='comment',
            new_name='comments',
        ),
        migrations.RemoveField(
            model_name='postit',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.AddField(
            model_name='postit',
            name='topic',
            field=models.ManyToManyField(blank=True, related_name='generated_category', to='forum.Category'),
        ),
    ]