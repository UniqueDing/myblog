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
from django.views.generic import RedirectView

from app import views as app_view

urlpatterns = [
    path('', app_view.index),
    path('article', app_view.article),
    path('article/<str:label>', app_view.articleLabel),
    path('picture', app_view.picture),
    path('picture/<str:label>', app_view.pictureLabel),
    path('music', app_view.music),
    path('about/', app_view.about),
    path('adetail/<int:id>', app_view.adetail),
    path('pdetail/<int:id>', app_view.pdetail),
    path('articleList/', app_view.articleList),
    path('labelList/', app_view.labelList),
    path('pictureList/', app_view.pictureList),
    path('plabelList/', app_view.plabelList),
    path('admin/', admin.site.urls),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),
]



#handler404 = app_view.index
#handler500 = app_view.index
