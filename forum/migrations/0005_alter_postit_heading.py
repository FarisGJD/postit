# Generated by Django 3.2.13 on 2022-05-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20220526_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postit',
            name='heading',
            field=models.CharField(blank=True, max_length=300, unique=True),
        ),
    ]