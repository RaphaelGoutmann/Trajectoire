from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 

from trajectoire import settings

from .views import *

urlpatterns = [
    path('', HomeView, name="home"),
    path('contribute', ContributeView, name="contribute"),

    path('search', SearchView.as_view(), name="search"),

    path('category/<str:slug>', CategoryDetailView.as_view(), name="category"),
    path('article/<str:slug>', ArticleDetailView.as_view(), name="article"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
