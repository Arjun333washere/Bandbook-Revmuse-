# Generated by Django 4.2.2 on 2023-06-13 02:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0002_band_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='availability',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]