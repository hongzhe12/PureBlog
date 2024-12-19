import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mdeditor.fields import MDTextField
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


def generate_random_slug():
    return str(uuid.uuid4())[:8]  # 生成一个8字符长的随机slug


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="文章标题")  # 文章标题
    slug = models.SlugField(max_length=200, unique=True, blank=True, default=generate_random_slug,
                            verbose_name="URL别名")  # 设置默认slug值
    summary = models.TextField(max_length=500, verbose_name="文章摘要")  # 文章摘要
    content = MDTextField(verbose_name="文章内容")  # 文章内容
    published_date = models.DateTimeField(default=timezone.now, verbose_name="发布时间")  # 发布时间
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  # 创建时间
    updated_date = models.DateTimeField(auto_now=True, verbose_name="更新时间")  # 更新时间

    class Meta:
        ordering = ['-published_date']  # 按发布时间降序排序
        verbose_name = "文章"
        verbose_name_plural = "文章"
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug])  # 生成文章详情页的URL

    def save(self, *args, **kwargs):
        if not self.slug:  # 如果slug为空，则设置默认值
            self.slug = generate_random_slug()
        super().save(*args, **kwargs)


class Comment(MPTTModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='文章'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='评论者'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='父评论'
    )
    content = models.TextField(verbose_name='评论内容')
    created_time = models.DateTimeField( verbose_name='创建时间',default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='是否可见')

    class MPTTMeta:
        order_insertion_by = ['created_time']

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'

