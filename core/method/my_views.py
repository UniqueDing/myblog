from django.shortcuts import render
from method.change_language import language
from method.md2html import md2html
from method.page_list import page_list
from pyquery import PyQuery as pq
from article import models
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

def music_view(request):
    lang = language(request)
    dict = {'lang': lang}
    return dict


def about_view(request):
    lang = language(request)
    dict = {'lang': lang}
    return dict

