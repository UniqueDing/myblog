"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views import static
from django.views.generic import RedirectView, TemplateView

from core import views as core_view
from article import views as article_view
from picture import views as picture_view
from movie import views as movie_view

urlpatterns = [
    path('', core_view.index),
    path('article', article_view.article),
    path('article/<str:label>', article_view.articleLabel),
    path('picture', picture_view.picture),
    path('picture/<str:label>', picture_view.pictureLabel),
    path('movie', movie_view.movie),
    path('movieset', movie_view.movieset),
    path('movieget', movie_view.movieget),
    path('about/', core_view.about),
    path('adetail/<int:id>', article_view.adetail),
    path('pdetail/<int:id>', picture_view.pdetail),
    path('articleList/', article_view.articleList),
    path('labelList/', article_view.labelList),
    path('pictureList/', picture_view.pictureList),
    path('plabelList/', picture_view.plabelList),
    path('btding/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=r'static/favicon.ico')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]

# handler404 = core_view.index
# handler500 = core_view.index
