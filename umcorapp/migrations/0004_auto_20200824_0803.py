# Generated by Django 3.1 on 2020-08-24 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umcorapp', '0003_news'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutUs',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
