from method.change_language import language
from django.http import Http404
from method.md2html import md2html
from method.page_list import page_list
from pyquery import PyQuery as pq
from article import models
import json
import math


def article_view(request):
    lang = language(request)
    try:
        labels = list(models.Article.objects.values_list('label', flat=True))
    except models.Article.DoesNotExist:
        raise Http404("labels does not exist")
    label_set = set(labels)
    my_list = []
    for ele in label_set:
        my_list.append("<a class=\"nav-link\" href=\"/article/" + ele + "\">" + ele + "&nbsp;&nbsp;("
                       + str(labels.count(ele)) + ")</a>")
    context = {'lang': lang, 'list': my_list}
    return context


def articleLabel_view(request, label):
    lang = language(request)
    try:
        labels = list(models.Article.objects.values_list('label', flat=True))
    except models.Article.DoesNotExist:
        raise Http404("labels does not exist")
    label_set = set(labels)
    my_list = []
    for ele in label_set:
        my_list.append("<a class=\"nav-link\" href=\"/article/" + ele + "\">" + ele + "&nbsp;&nbsp;(" + str(
            labels.count(ele)) + ")</a>")
    context = {'lang': lang, 'list': my_list, 'label': label}
    return context


def adetail_view(request, id):
    lang = language(request)
    try:
        name = models.Article.objects.values('name').get(id=id)
    except models.Article.DoesNotExist:
        raise Http404("name does not exist")
    f = open('static/md/' + name['name'] + '/' + name['name'] + '.md', encoding='UTF-8')
    file = f.read()
    # print(file)
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
        #     list_index = (int(ele.__html__()[2]))1
        space = ''
        print(ele.__html__())
        for i in range(int(ele.__html__()[2]) - 1):
            space += '&nbsp;·&nbsp;'
        button_list.append("<a class=\"nav-link \" href=\"#" + ele.attr(
            "id") + "\">" + space + ele.text() + "</a>")
    context = {'lang': lang, 'md': file, 'file_name': name['name'], 'list': button_list}
    return context


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
