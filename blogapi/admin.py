from django.contrib import admin
from .models import Article, ArticleTag
from django.utils.text import slugify

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (slugify('title'),),
    }
admin.site.register(Article, ArticleAdmin)

class ArticleTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (slugify('name'),),
    }
admin.site.register(ArticleTag, ArticleTagAdmin)