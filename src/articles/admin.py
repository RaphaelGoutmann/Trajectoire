from django.contrib import admin

from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ["name", "description", "thumbnail"]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",
                    "author",
                    "category",
                    "last_updated")

    fields = ["title", "author", "category", "resume", "thumbnail", "content"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

admin.site.site_header = ""