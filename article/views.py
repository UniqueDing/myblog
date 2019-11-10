from django.http import HttpResponse
from django.shortcuts import render
from article.method import my_views


def article(request):
    dict = my_views.article_view(request)
    return render(request, 'article.html', dict)


def articleLabel(request, label):
    dict = my_views.articleLabel_view(request, label)
    return render(request, 'article.html', dict)


def picture(request):
    dict = my_views.picture_view(request)
    return render(request, 'picture.html', dict)


def pictureLabel(request, label):
    dict = my_views.pictureLabel_view(request, label)
    return render(request, 'picture.html', dict)


def pictureList(request):
    text = my_views.pictureList_view(request)
    return HttpResponse(text)


def plabelList(request):
    text = my_views.plabelList_view(request)
    return HttpResponse(text)


def adetail(request, id):
    dict = my_views.adetail_view(request, id)
    return render(request, 'adetail.html', dict)

def pdetail(request,id):
    dict = my_views.pdetail_view(request,id)
    return render(request, 'pdetail.html', dict)

def articleList(request):
    text = my_views.articleList_view(request)
    return HttpResponse(text)


def labelList(request):
    text = my_views.labelList_view(request)
    return HttpResponse(text)
