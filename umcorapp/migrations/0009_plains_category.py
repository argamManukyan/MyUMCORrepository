# Generated by Django 3.1 on 2020-08-24 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umcorapp', '0008_auto_20200824_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='plains',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='plains', to='umcorapp.plainscategory'),
            preserve_default=False,
        ),
    ]
