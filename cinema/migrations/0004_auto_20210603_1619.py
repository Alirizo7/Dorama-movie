# Generated by Django 3.1.7 on 2021-06-03 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(db_index=True, upload_to='', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.AlterField(
            model_name='movie',
            name='about',
            field=models.TextField(blank=True, verbose_name='О фильме'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=225, verbose_name='Режисёр'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, db_index=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='money',
            field=models.IntegerField(blank=True, default=0, verbose_name='Бюджет'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Траилер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.CharField(blank=True, max_length=225, verbose_name='Сценарист'),
        ),
        migrations.AddField(
            model_name='movie',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.collection'),
        ),
    ]
