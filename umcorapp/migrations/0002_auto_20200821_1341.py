# Generated by Django 3.1 on 2020-08-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umcorapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
