# Generated by Django 2.2 on 2020-05-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20200501_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=22, unique=True),
            preserve_default=False,
        ),
    ]
