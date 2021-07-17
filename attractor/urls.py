"""attractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from attractor.views import IndexView, AddCategoryView, AddArticleView, RegisterView, ProfileView, LogoutView, \
    ListView, EditArticleView, DeleteArticleView, EditCategoryView, DeleteCategoryView, UpdatePasswordView, \
    DeleteProfileView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    path('add_article/', AddArticleView.as_view(), name="add-article"),
    path('list/<int:article_id>/edit_article', EditArticleView.as_view(), name="edit-article"),
    path('list/<int:category_id>/edit_category', EditCategoryView.as_view(), name="edit-category"),
    path('list/<int:article_id>/delete_article', DeleteArticleView.as_view(), name="delete-article"),
    path('list/<int:category_id>/delete_category', DeleteCategoryView.as_view(), name="delete-category"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('accounts/register/', RegisterView.as_view(), name="register"),
    path('accounts/profile/', ProfileView.as_view(), name="profile"),
    path('accounts/edit_profile/', UpdatePasswordView.as_view(), name="update-password"),
    path('account/delete_profile/', DeleteProfileView.as_view(), name="delete-profile"),
    path('list/', ListView.as_view(), name="list"),
    path('api_views/', include("attractor.api_views.urls")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
