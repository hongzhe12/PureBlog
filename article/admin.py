from django.contrib import admin
from .models import Article
from mptt.admin import MPTTModelAdmin
from .models import Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published_date', 'created_date', 'updated_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}  # 自动根据标题生成slug
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)


admin.site.register(Article, ArticleAdmin)


admin.site.site_header = '博客管理后台'  # 设置header
admin.site.site_title = '博客管理后台'   # 设置title
admin.site.index_title = '博客管理后台'

@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin):
    list_display = ('user', 'article', 'content', 'created_time', 'is_active')
    list_filter = ('is_active', 'created_time')
    search_fields = ('content', 'user__username', 'article__title')