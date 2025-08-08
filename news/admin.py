from django.contrib import admin
from .models import Source, Article, Incident

admin.site.register(Source)
admin.site.register(Article)
admin.site.register(Incident)
