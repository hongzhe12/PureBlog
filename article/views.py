import markdown
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Article


def article_list(request):
    articles = Article.objects.all()  # 获取所有文章
    paginator = Paginator(articles, 5)  # 每页显示5篇文章
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'articles': page_obj, 'title': '文章首页'}
    return render(request, 'blog/article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)  # 根据slug获取对应的文章

    # 将markdown语法渲染成html样式
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            # 包含 缩写、表格等常用扩展
                                            'markdown.extensions.extra',
                                            # 语法高亮扩展
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.tables',
                                        ])

    context = {'article': article, 'title': article.title}

    return render(request, 'blog/article_detail.html', context)


def about_view(request):
    context = {
        'title': '关于我',
    }
    return render(request, 'blog/about.html',context)


def contact_view(request):
    context = {
        'title': '联系我',
    }
    return render(request, 'blog/contact.html',context)


def error_view(request):
    raise Http404("这是一个人为抛出的404错误")
