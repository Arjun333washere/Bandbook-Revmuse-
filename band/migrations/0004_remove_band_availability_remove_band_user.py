# Generated by Django 4.2.2 on 2023-06-13 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0003_band_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='band',
            name='user',
        ),
    ]
