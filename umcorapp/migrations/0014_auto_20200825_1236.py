# Generated by Django 3.1 on 2020-08-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umcorapp', '0013_donate_donated'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='name_hy',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_hy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]
