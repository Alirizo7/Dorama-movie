# Generated by Django 3.1.7 on 2021-05-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=False, verbose_name='Публиковать'),
        ),
    ]