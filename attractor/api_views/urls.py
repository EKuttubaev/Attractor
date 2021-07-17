from django.urls import path

from attractor.api_views.views import CategoriesListApiView, ArticleListApiView

urlpatterns = [
    path("categories/", CategoriesListApiView.as_view()),
    path("articles/", ArticleListApiView.as_view())
]