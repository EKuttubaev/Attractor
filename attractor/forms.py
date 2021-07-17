from django.forms import ModelForm

from attractor.models import Category, Article


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = []


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = []
