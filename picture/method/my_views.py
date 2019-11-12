from method.change_language import language
from django.http import Http404
from method.md2html import md2html
from method.page_list import page_list
from pyquery import PyQuery as pq
from picture import models
import json
import math


def picture_view(request):
    lang = language(request)
    try:
        labels = list(models.Picture.objects.values_list('label', flat=True))
    except models.Picture.DoesNotExist:
        raise Http404("labels does not exist")
    label_set = set(labels)
    my_list = []
    for ele in label_set:
        my_list.append("<a class=\"nav-link\" href=\"/picture/" + ele + "\">" + ele + "&nbsp;&nbsp;(" + str(
            labels.count(ele)) + ")</a>")
    context = {'lang': lang, 'list': my_list}
    return context


def pictureLabel_view(request, label):
    lang = language(request)
    try:
        labels = list(models.Picture.objects.values_list('label', flat=True))
    except models.Picture.DoesNotExist:
        raise Http404("labels does not exist")
    label_set = set(labels)
    my_list = []
    for ele in label_set:
        my_list.append("<a class=\"nav-link\" href=\"/picture/" + ele + "\">" + ele + "&nbsp;&nbsp;(" + str(
            labels.count(ele)) + ")</a>")
    context = {'lang': lang, 'list': my_list, 'label': label}
    return context


def pdetail_view(request, id):
    lang = language(request)
    try:
        my_list = models.Picture.objects.values().get(id=id)
    except models.Picture.DoesNotExist:
        raise Http404("labels does not exist")
    pic = '../static/pic/' + my_list['name'] + '.jpg'
    file = open('static/pic/' + my_list['name'] + '.txt', encoding='UTF-8')
    detail = file.read()
    file.close()
    context = {'name': my_list['name'], 'pic': pic, 'author': my_list['author'], 'time': my_list['time'], 'detail': detail,
            'label': my_list['label']}
    return context


def pictureList_view(request):
    page = int(request.GET.get('page', None))
    order = ['true', 'false', 'false', 'true', 'true', 'false', 'false', 'true']
    list = []
    for ind, ele in enumerate(models.Picture.objects.all().order_by('-time')[(page * 8 - 8):(page * 8)]):
        f = open('static/pic/' + ele.name + '.txt', encoding='UTF-8')
        detail = f.read()[0:20]
        f.close()
        pic = '../static/pic/' + ele.name + '.jpg'
        dict = {'id': ele.id, 'name': ele.name, 'author': ele.author, 'time': str(ele.time), 'label': ele.label,
                'detail': detail, 'pic': pic, 'order': order[ind]}
        list.append(dict)
    count = math.ceil(models.Picture.objects.count() / 8)
    text = json.dumps({'list': list, 'page': page, 'pageList': page_list(page, count), 'totalPage': count})
    return text


def plabelList_view(request):
    page = int(request.GET.get('page', None))
    label = request.GET.get('label', None)
    order = ['true', 'false', 'false', 'true', 'true', 'false']
    list = []
    # - time 逆序
    for ind, ele in enumerate(
            models.Picture.objects.filter(label__exact=label).order_by('-time')[(page * 8 - 8):(page * 8)]):
        f = open('static/pic/' + ele.name + '.txt', encoding='UTF-8')
        detail = f.read()[0:20]
        f.close()
        pic = '../static/pic/' + ele.name + '.jpg'
        dict = {'id': ele.id, 'name': ele.name, 'author': ele.author, 'time': str(ele.time), 'label': ele.label,
                'detail': detail, 'pic': pic, 'order': order[ind]}
        list.append(dict)
    count = math.ceil(models.Picture.objects.filter(label__exact=label).count() / 8)
    if count == 0:
        return 0
    text = json.dumps({'list': list, 'page': page, 'pageList': page_list(page, count), 'totalPage': count})
    return text


def labelList_view(request):
    page = int(request.GET.get('page', None))
    label = request.GET.get('label', None)
    list = []
    # - time 逆序
    for ele in models.Article.objects.filter(label__exact=label).order_by('-time')[(page * 10 - 10):(page * 10)]:
        f = open('static/md/' + ele.name + '/' + ele.name + '.md', encoding='UTF-8')
        file = f.read()[:200]
        file = md2html(file)
        p = pq(file)
        f.close()
        dict = {'id': ele.id, 'name': ele.name, 'author': ele.author, 'time': str(ele.time)[:7],
                'data': str(ele.time)[-2:], 'label': ele.label,
                'detail': p.text()}
        list.append(dict)
    count = math.ceil(models.Article.objects.filter(label__exact=label).count() / 10)
    if count == 0:
        return 0
    text = json.dumps({'list': list, 'page': page, 'pageList': page_list(page, count), 'totalPage': count})
    return text
