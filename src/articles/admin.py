from django.contrib import admin

from .models import Category, Article, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ["name", "description"]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",
                    "author",
                    "category",
                    "last_updated",
                    "views")

    fields = ["title", "author", "category", "resume", "thumbnail", "content"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "article", "content", "date")
    fields = ["author", "article", "content"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_header = ""