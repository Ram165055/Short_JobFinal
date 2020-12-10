# Generated by Django 3.1 on 2020-10-31 06:56

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('pagelink', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
