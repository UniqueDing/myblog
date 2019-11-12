from django.shortcuts import render
from django.http import HttpResponse
from picture.method import my_views

# Create your views here.


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


def pdetail(request,id):
    dict = my_views.pdetail_view(request,id)
    return render(request, 'pdetail.html', dict)


def labelList(request):
    text = my_views.labelList_view(request)
    return HttpResponse(text)