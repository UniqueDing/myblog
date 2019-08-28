from django.contrib import admin

from .models import Article
from .models import Picture

admin.site.register(Article)
admin.site.register(Picture)
