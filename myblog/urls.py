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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView

from core import views as core_view
from article import views as article_view
from picture import views as picture_view

urlpatterns = [
    path('', core_view.index),
    path('article', article_view.article),
    path('article/<str:label>', article_view.articleLabel),
    path('picture', article_view.picture),
    path('picture/<str:label>', article_view.pictureLabel),
    path('music', core_view.music),
    path('about/', core_view.about),
    path('adetail/<int:id>', article_view.adetail),
    path('pdetail/<int:id>', article_view.pdetail),
    path('articleList/', article_view.articleList),
    path('labelList/', article_view.labelList),
    path('pictureList/', article_view.pictureList),
    path('plabelList/', article_view.plabelList),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=r'static/favicon.ico')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

]


handler500 = core_view.index
