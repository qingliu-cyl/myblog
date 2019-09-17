from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404

from article.models import ArticlePost,ArticleColumn

# Create your views here.
def article_list(request,article_column):
    articles_list = ArticlePost.objects.filter(column__column = article_column)
    columns = ArticleColumn.objects.all()
    paginator = Paginator(articles_list,5)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    return render(request,"blog/article_list.html",{"articles":articles,"columns":columns,"page":current_page})

def blog(request):
    articles_list = ArticlePost.objects.all()
    columns = ArticleColumn.objects.all()
    paginator = Paginator(articles_list,5)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    return render(request,"blog/blog.html",{"articles":articles,"columns":columns,"page":current_page})

def article_detail(request,id,slug):
    columns = ArticleColumn.objects.all()
    article = get_object_or_404(ArticlePost,id = id,slug = slug)
    return render(request,"blog/article_detail.html",{"article":article,"columns":columns})
    
