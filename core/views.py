from django.shortcuts import render
import core.method.my_views as my_views
# Create your views here.


def index(request):
    context = my_views.index_view(request)
    return render(request, 'index.html', context)


def about(request):
    context = my_views.about_view(request)
    return render(request, 'about.html', context)


def music(request):
    context = my_views.music_view(request)
    return render(request, 'music.html', context)
