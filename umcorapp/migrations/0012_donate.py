# Generated by Django 3.1 on 2020-08-24 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umcorapp', '0011_maincontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_group', models.CharField(max_length=120)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('total_amount', models.FloatField(default=0.0)),
                ('sphere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umcorapp.plainscategory')),
            ],
        ),
    ]
