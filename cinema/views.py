from django.shortcuts import render, redirect, reverse
from .models import Post, Movie, Collection
from .form import Register


# Create your views here.

def index(request):
    news_images = Post.objects.filter(public=True)
    movies = Movie.objects.filter(public=True, pk__lte=4)
    movies2 = Movie.objects.filter(public=True, pk__gte=4)
    collections = Collection.objects.all()
    context = {'news_images': news_images, 'movies': movies, 'collections': collections, 'movies2': movies2}
    return render(request, 'cinema/index.html', context)


def movie_detail_2(request, slug):
    movies2 = Movie.objects.get(slug__exact=slug)
    movies2.view += 1
    movies2.save()
    return render(request, 'cinema/movie_detail.html', {'movies2': movies2})


def movie_detail(request, slug):
    movies = Movie.objects.get(slug__exact=slug)
    movies.view += 1
    movies.save()
    return render(request, 'cinema/movie_detail.html', {'movies': movies})


def collection_detail(request, slug):
    collection = Collection.objects.get(slug__exact=slug)
    return render(request, 'cinema/collection_detail.html', {'collection': collection})


def register(request):
    if request.method == 'POST':
        form = Register(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Register()
    return render(request, 'cinema/register.html', {'form': form})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'news/profile.html')


def comment(request, slug):
    if request.user.is_authenticated:
        movies = Movie.objects.get(slug__iexact=slug)
        if request.method == 'POST':
            movies.comment_set.create(
                user=request.user,
                text=request.POST.get('text')
            )
    return redirect(reverse('movie_detail_url', kwargs={'slug': slug}))
