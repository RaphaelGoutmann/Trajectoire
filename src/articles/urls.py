from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 

from trajectoire import settings

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contribute', ContributeView, name="contribute"),

    path('search', SearchView.as_view(), name="search"),

    path('category/<str:slug>', CategoryDetailView.as_view(), name="category"),
    path('article/<str:slug>', ArticleDetailView.as_view(), name="article"),

    path('editorjs/', include('django_editorjs_fields.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
