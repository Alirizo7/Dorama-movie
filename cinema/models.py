from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models here.

class Collection(models.Model):
    title = models.CharField('Заголовок', max_length=255, db_index=True)
    slug = models.SlugField('Ссылка', max_length=255, unique=True)
    image = models.ImageField('Картинка', db_index=True)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.title

    def link(self):
        return reverse('collection_detail_url', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255, db_index=True)
    image = models.ImageField('Картинка', db_index=True)
    public = models.BooleanField('Публиковать', default=False)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField('Название', max_length=225, db_index=True)
    image = models.ImageField('Картинка', db_index=True, blank=True)
    public = models.BooleanField('Публиковать', default=False)
    slug = models.SlugField('Ссылка', unique=True)
    date = models.DateField('Дата', default=timezone.now)
    view = models.IntegerField('Просмотры', default=0)
    video = models.FileField('Трейлер', null=True)
    money = models.IntegerField('Бюджет', blank=True, default=0)
    director = models.CharField('Режисёр', max_length=225, blank=True)
    writer = models.CharField('Сценарист', max_length=225, blank=True)
    about = models.TextField('О фильме', blank=True)
    country = models.CharField('Страна', max_length=225)
    collection = models.ForeignKey('Collection', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title

    def link(self):
        return reverse('movie_detail_url', kwargs={'slug': self.slug})


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Photo', null=True, blank=True, upload_to='user/avatar/')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователы'

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField('text')
    date = models.DateTimeField('date', default=timezone.now)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return "User:" + self.user.username + '|date' + str(self.date)
