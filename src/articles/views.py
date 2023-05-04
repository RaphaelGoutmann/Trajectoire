from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import *

def ArticleDetailView(request, slug):
    article = get_object_or_404(Article, slug=slug)
    recommandations = Article.objects.all().exclude(slug=slug)[:3]
    return render(request, 'articles/article_detail.html', {'article': article,
                                                            'recommandations': recommandations })

def CategoryDetailView(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'articles/category_detail.html', {'category': category})

def HomeView(request):
    articles = Article.objects.all()
    return render(request, 'articles/home.html', {'articles': articles})

def ContributeView(request):
    return render(request, 'articles/contribute.html')


def SearchView(request):
    results = None
    query = ''

    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            results = Article.objects.filter( Q(title__icontains=query) | Q(content__icontains=query) )
            
    return render(request, 'articles/search.html', {'results': results, 'query': query})