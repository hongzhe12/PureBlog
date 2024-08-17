from django.db import models
from django.urls import reverse
from django.utils import timezone
from mdeditor.fields import MDTextField


class Article(models.Model):
    title = models.CharField(max_length=200)  # 文章标题
    slug = models.SlugField(max_length=200, unique=True)  # 用于URL的slug
    summary = models.TextField(max_length=500)  # 文章摘要
    content = MDTextField(verbose_name="文章内容")  # 文章内容
    published_date = models.DateTimeField(default=timezone.now)  # 发布时间
    created_date = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated_date = models.DateTimeField(auto_now=True)  # 更新时间

    class Meta:
        ordering = ['-published_date']  # 按发布时间降序排序

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug])  # 生成文章详情页的URL
