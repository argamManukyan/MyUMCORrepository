# Generated by Django 3.1 on 2020-08-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umcorapp', '0002_auto_20200821_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
