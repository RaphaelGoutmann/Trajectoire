from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import CommentForm

from .models import *

def ArticleDetailView(request, slug):
    article = get_object_or_404(Article, slug=slug)
    recommandations = Article.objects.all().exclude(slug=slug)[:3]

    comments = article.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'articles/article_detail.html', {'article': article,
                                                            'recommandations': recommandations,
                                                            'comments': comments,
                                                            'comment_form': comment_form })

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