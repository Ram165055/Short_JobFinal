# Generated by Django 3.1 on 2021-05-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagelink', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='destination',
            name='skill',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
