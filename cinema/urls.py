from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("cinema/<slug:slug>/", views.movie_detail, name='movie_detail_url'),
    path("cinema/<slug:slug>/", views.movie_detail_2, name='movie_detail_url'),
    path("collection/<slug:slug>/", views.collection_detail, name='collection_detail_url'),
    path("register/", views.register, name='register'),
    path("profile/", views.profile, name='profile_url'),
    path("collection/<slug:slug>/comment", views.comment, name='comment_url')
]
