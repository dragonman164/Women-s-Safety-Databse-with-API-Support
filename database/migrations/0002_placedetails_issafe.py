# Generated by Django 3.1.4 on 2020-12-14 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placedetails',
            name='issafe',
            field=models.BooleanField(default=True),
        ),
    ]