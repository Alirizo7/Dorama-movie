# Generated by Django 3.1.7 on 2021-07-01 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_auto_20210701_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='film',
        ),
    ]
