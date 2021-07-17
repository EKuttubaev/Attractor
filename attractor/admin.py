from django.contrib.admin import site, ModelAdmin

from attractor.models import Category, Article


class CategoryAdmin(ModelAdmin):
    exclude = []


class ArticleAdmin(ModelAdmin):
    exclude = []


site.register(Category, CategoryAdmin)
site.register(Article, ArticleAdmin)
