from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from attractor.forms import CategoryForm, ArticleForm
from attractor.models import Category, Article


class IndexView(TemplateView):
    template_name = "index.html"


class AddCategoryView(TemplateView):
    template_name = "category.html"

    def dispatch(self, request, *args, **kwargs):
        form = CategoryForm()

        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form = form.save()
                return redirect("/")
        return render(request, self.template_name, {
            "form": form
        })


class AddArticleView(TemplateView):
    template_name = "article.html"

    def dispatch(self, request, *args, **kwargs):
        form = ArticleForm()

        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                form = form.save()
                return redirect("/")
        return render(request, self.template_name, {
            "form": form
        })


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse("login"))
        return render(request, self.template_name, {
            "form": form
        })


class ProfileView(TemplateView):
    template_name = "profile.html"

    def dispatch(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, self.template_name, context={
            'users': users
        })


class UpdatePasswordView(TemplateView):
    template_name = "update_password.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect("/")
        else:
            form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {
            'form': form
        })


class DeleteProfileView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        user_id = self.request.user.id
        User.objects.get(id=user_id).delete()
        return redirect("/")

class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class ListView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        categories = Category.objects.all()
        articles = Article.objects.all()
        return render(request, "list.html", context={
            "categories": categories,
            "articles": articles
        })


class EditArticleView(TemplateView):
    template_name = "edit_article.html"

    def dispatch(self, request, *args, **kwargs):
        article_id = kwargs['article_id']
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect("/")
        return render(request, self.template_name, {
            "form": form
        })


class EditCategoryView(TemplateView):
    template_name = "edit_category.html"

    def dispatch(self, request, *args, **kwargs):
        category_id = kwargs['category_id']
        category = Category.objects.get(id=category_id)
        form = CategoryForm(instance=category)
        if request.method == "POST":
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect("/")
        return render(request, self.template_name, {
            "form": form
        })


class DeleteArticleView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        article_id = kwargs['article_id']
        Article.objects.get(id=article_id).delete()
        return redirect("/")


class DeleteCategoryView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        category_id = kwargs['category_id']
        Category.objects.get(id=category_id).delete()
        return redirect("/")
