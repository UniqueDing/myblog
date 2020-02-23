from method.change_language import language
from pyquery import PyQuery as pq
from django.http import Http404
from movie import models
import json
import math


def movie_view(request):
    lang = language(request)
    changed = request.GET.get('changed', None)
    try:
        movie_url = models.Movie.objects.values('url').get(id=1)
        movie_status = models.Movie.objects.values('status').get(id=1)
        movie_rate = models.Movie.objects.values('rate').get(id=1)
        movie_changed = models.Movie.objects.values('changed').get(id=1)
    except models.Movie.DoesNotExist:
        raise Http404("does not exist")
    if str(movie_changed['changed']) == changed:
        is_admin = 'display'
    else:
        is_admin = 'none'
    print(str(movie_changed['changed']) + ' ' + str(changed))
    context = {
                'lang': lang,
                'movie_url' : movie_url['url'],
                'movie_status' : movie_status['status'],
                'movie_rate' : movie_rate['rate'],
                'movie_changed' : is_admin,
    }
    return context


def movieset_view(request):
    movie_changed = models.Movie.objects.values('changed').get(id=1)
    if str(movie_changed['changed']) == request.GET.get('movie_changed', None):
        models.Movie.objects.filter(id='1').update(url=request.GET.get('movie_url', None))
        models.Movie.objects.filter(id='1').update(status=request.GET.get('movie_status', None))
        models.Movie.objects.filter(id='1').update(rate=request.GET.get('movie_rate', None))
        return 'true'
    return 'false'


def movieget_view(request):
    movie_url = models.Movie.objects.values('url').get(id=1)
    movie_status = models.Movie.objects.values('status').get(id=1)
    movie_rate = models.Movie.objects.values('rate').get(id=1)
    context = {
                'movie_url' : movie_url['url'],
                'movie_status' : movie_status['status'],
                'movie_rate' : movie_rate['rate']
    }
    text = json.dumps(context)
    return text
