from django.http import JsonResponse
from django.views import View

from attractor.models import Category, Article

#http://127.0.0.1:8000/api_views/categories/
class CategoriesListApiView(View):
    def dispatch(self, request, *args, **kwargs):
        categories = Category.objects.all()
        categories_data = []
        for category in categories:
            category_data = {
                "id": category.id,
                "title": category.title,
                "parent_id": category.parent_id
            }
            categories_data.append(category_data)
        return JsonResponse(categories_data, safe=False)

#http://127.0.0.1:8000/api_views/articles/
class ArticleListApiView(View):
    def dispatch(self, request, *args, **kwargs):
        articles = Article.objects.all()
        articles_data = []
        for article in articles:
            article_data = {
                "id": article.id,
                "category_id": article.category_id,
                "user_id": article.user_id,
                "title": article.title,
                "description": article.description,
                "image": article.image.url
            }
            articles_data.append(article_data)
        return JsonResponse(articles_data, safe=False)
