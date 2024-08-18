from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.article_list, name='home'),  # 主页，显示文章列表
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),  # 文章详情页
    path('about/', views.about_view, name='about'),  # 文章详情页
    path('contact/', views.contact_view, name='contact'),  # 文章详情页
    path('error/', views.error_view),  # 错误页
]
