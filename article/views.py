import markdown
from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Article, Comment


def article_list(request):
    articles = Article.objects.all()  # 获取所有文章
    paginator = Paginator(articles, 5)  # 每页显示5篇文章
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'articles': page_obj, 'title': '文章首页'}
    return render(request, 'blog/article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    # 获取文章的所有评论
    comments = Comment.objects.filter(article=article, is_active=True)
    
    # 将markdown语法渲染成html样式
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.tables',
                                        ])

    context = {
        'article': article, 
        'title': article.title,
        'comments': comments
    }
    
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


@login_required
def post_comment(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        parent_id = request.POST.get('parent_id', None)
        content = request.POST.get('content')

        if not content:
            return JsonResponse({'status': 'error', 'message': '评论内容不能为空'})

        # 创建评论对象
        comment = Comment(
            article=article,
            user=request.user,
            content=content
        )

        # 如果有父评论，设置父评论
        if parent_id:
            parent_comment = Comment.objects.get(id=parent_id)
            comment.parent = parent_comment

        comment.save()

        # 返回评论数据
        return JsonResponse({
            'status': 'success',
            'data': {
                'id': comment.id,
                'content': comment.content,
                'username': comment.user.username,
                'created_time': comment.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                'parent_id': parent_id
            }
        })
    
    return JsonResponse({'status': 'error', 'message': '仅支持POST请求'})
