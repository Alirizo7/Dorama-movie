# Generated by Django 3.1.7 on 2021-06-22 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema', '0004_auto_20210603_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Трейлер'),
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user/avatar/', verbose_name='Photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователы',
            },
        ),
    ]
