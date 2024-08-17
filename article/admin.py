from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published_date', 'created_date', 'updated_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}  # 自动根据标题生成slug
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)


admin.site.register(Article, ArticleAdmin)
