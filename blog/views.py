from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse,JsonResponse
from .models import Article,Category
# Create your views here.


def home(request,page=1):
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 4)
    articles = paginator.get_page(page)
    contex = {
        "articles" : articles,
    }
    return render(request,"blog/home.html",contex)

def detail(request,slug):
    contex = {
        "article" : get_object_or_404(Article.objects.published(),slug=slug)
    }
    return render(request,"blog/detail.html",contex)

def category(request,slug):
    contex = {
        "category" : get_object_or_404(Category,slug=slug,status=True)
    }
    return render(request,"blog/category.html",contex)