from django.views.generic import DetailView, ListView
from django.shortcuts import render

from .models import *

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'articles/category_detail.html'
    context_object_name = 'category'

class HomeView(ListView):
    model = Article
    template_name = 'articles/home.html'
    context_object_name = 'articles'

def ContributeView(request):
    return render(request, 'articles/contribute.html')

class SearchView(ListView):
    model = Article
    template_name = 'articles/search.html'
    context_object_name = 'results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('query')

       if query:
          postresult = Article.objects.filter(title__icontains=query)
          result = postresult
       else:
           result = None

       return result