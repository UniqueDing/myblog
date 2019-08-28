from django.shortcuts import render
from app.method.change_language import language
from app.method.md2html import md2html
from app.method.page_list import page_list
from pyquery import PyQuery as pq
from app import models
import json
import math


def index_view(request):
    lang = language(request)
    article = []
    picture = []
    for ele in models.Article.objects.all().order_by('-time')[:8]:
        f = open('static/md/' + ele.name + '/' + ele.name + '.md', encoding='UTF-8')
        file = f.read()[:200]
        file = md2html(file)
        p = pq(file)
        f.close()
        dic = {'id': ele.id, 'name': ele.name, 'author': ele.author, 'time': str(ele.time)[:7],
               'data': str(ele.time)[-2:], 'label': ele.label,
               'detail': p.text()}
        article.append(dic)
    for ele in models.Picture.objects.all().order_by('-time')[:4]:
        f = open('static/pic/' + ele.name + '.txt', encoding='UTF-8')
        detail = f.read()[0:20]
        f.close()
        pic = '../static/pic/' + ele.name + '.jpg'
        dic = {'id': ele.id, 'name': ele.name, 'author': ele.author, 'time': str(ele.time), 'label': ele.label,
               'detail': detail, 'pic': pic}
        picture.append(dic)
    dict = {'lang': lang, 'articles': article, 'pictures': picture}
    return dict


def article_view(request):
    lang = language(request)
    labels = list(models.Article.objects.values_list('label', flat=True))
    labelset = set(labels)
    mylist = []
    for ele in labelset:
        mylist.append("<a class=\"nav-link\" href=\"/article/" + ele + "\">" + ele + "&nbsp;&nbsp;(" + str(
            labels.count(ele)) + ")</a>")
    dict = {'lang': lang, 'list': mylist}
    return dict


def articleLabel_view(request, label):
    lang = language(request)
    labels = list(models.Article.objects.values_list('label', flat=True))
    labelset = set(labels)
    mylist = []
    for ele in labelset:
        mylist.append("<a class=\"nav-link\" href=\"/article/" + ele + "\">" + ele + "&nbsp;&nbsp;(" + str(
            labels.count(ele)) + ")</a>")
    dict = {'lang': lang, 'list': mylist, 'label': label}
    return dict


def picture_view(request):
    lang = language(request)
    labels = list(models.Picture.objects.values_list('label', flat=True))
    labelset = set(labels)
    mylist = []
    for ele in labelset:
        mylist.append("<a class=\"nav-link\" href=\"/picture/" + ele + "\">" + ele + "&nbsp;&nbsp;(" + str(
            labels.count(ele)) + ")</a>")
    dict = {'lang': lang, 'list': mylist}
    return dict


def pictureLabel_view(request, label):
    lang = language(request)
    labels = list(models.Picture.objects.values_list('label', flat=True))
    labelset = set(labels)
    mylist = []
    for ele in labelset:
        mylist.append("<a class=\"nav-link\" href=\"/picture/" + ele + "\">" + ele + "&nbsp;&nbsp;(" + str(
            labels.count(ele)) + ")</a>")
    dict = {'lang': lang, 'list': mylist, 'label': label}
    return dict


def adetail_view(request, id):
    lang = language(request)
    name = models.Article.objects.values('name').get(id=id)
    f = open('static/md/' + name['name'] + '/' + name['name'] + '.md', encoding='UTF-8')
    file = f.read()
    print(file)
    f.close()
    # 解析md
    file = md2html(file)
    p = pq(file)
    # 生成目录
    button_list = []
    list_index = 0
    for ele in p(":header").items():
        # if int(ele.__html__()[2]) > list_index:
        #     list_index = (int(ele.__html__()[2]))
        #     print("+")
        #     button_list.append("<nav class=\"nav-pills\">")
        # elif int(ele.__html__()[2]) < list_index:
        #     for i in range(list_index - int(ele.__html__()[2])):
        #         button_list.append("</nav>")
        #         print("-")
        #     list_index = (int(ele.__html__()[2]))
        space = ''
        print(ele.__html__())
        for i in range(int(ele.__html__()[2]) - 1):
            space += '&nbsp;·&nbsp;'
        button_list.append("<a class=\"nav-link \" href=\"#" + ele.attr(
            "id") + "\">" + space + ele.text() + "</a>")
    # print(button_list)
    # print(file)
    dict = {'lang': lang, 'md': file, 'file_name': name['name'], 'list': button_list}
    return dict


def pdetail_view(request, id):
    lang = language(request)
    list = models.Picture.objects.values().get(id=id)
    print(list)
    pic = '../static/pic/' + list['name'] + '.jpg'
    file = open('static/pic/' + list['name'] + '.txt', encoding='UTF-8')
    detail = file.read()
    file.close()
    dict = {'name': list['name'], 'pic': pic, 'author': list['author'], 'time': list['time'], 'detail': detail,
            'label': list['label']}
    return dict


def music_view(request):
    lang = language(request)
    dict = {'lang': lang}
    return dict


def about_view(request):
    lang = language(request)
    dict = {'lang': lang}
    return dict


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


def articleList_view(request):
    page = int(request.GET.get('page', None))
    list = []
    for ele in models.Article.objects.all().order_by('-time')[(page * 10 - 10):(page * 10)]:
        f = open('static/md/' + ele.name + '/' + ele.name + '.md', encoding='UTF-8')
        file = f.read()[:200]
        file = md2html(file)
        p = pq(file)
        f.close()
        dict = {'id': ele.id, 'name': ele.name, 'author': ele.author, 'time': str(ele.time)[:7],
                'data': str(ele.time)[-2:], 'label': ele.label,
                'detail': p.text()}
        list.append(dict)
    count = math.ceil(models.Article.objects.count() / 10)
    text = json.dumps({'list': list, 'page': page, 'pageList': page_list(page, count), 'totalPage': count})
    #text = {'list': list, 'page': page, 'pageList': page_list(page, count), 'totalPage': count}
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
