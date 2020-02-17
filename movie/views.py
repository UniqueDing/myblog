from django.shortcuts import render
from django.http import HttpResponse
import movie.method.my_views as my_views
# Create your views here.


def movie(request):
    context = my_views.movie_view(request)
    return render(request, 'movie.html', context)


def movieset(request):
    text = my_views.movieset_view(request)
    return HttpResponse(text)

def movieget(request):
    text = my_views.movieget_view(request)
    return HttpResponse(text)
