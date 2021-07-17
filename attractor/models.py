from django.contrib.auth.models import User

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    parent_id = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name="id категории", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="id пользователя", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Заголовок статьи", max_length=255)
    description = models.CharField(verbose_name="Описание", max_length=255)
    image = models.ImageField(verbose_name="Иконка", upload_to="attrimg/", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
