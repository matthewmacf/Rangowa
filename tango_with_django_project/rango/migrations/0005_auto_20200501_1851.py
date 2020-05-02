# Generated by Django 2.2 on 2020-05-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_remove_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
