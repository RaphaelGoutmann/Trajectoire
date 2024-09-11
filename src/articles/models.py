from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User

# EditorJS
from django_editorjs_fields import EditorJsJSONField 

# Category Model

class Category(models.Model):
    name        = models.CharField(max_length=255, unique=True, verbose_name='Nom')
    description = models.CharField(max_length=255, verbose_name='Description')
    slug        = models.SlugField(max_length=255, unique=True, blank=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-id']

        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

# Article Model 

class Article(models.Model):
    title            = models.CharField(max_length=255, unique=True, verbose_name='Titre')
    slug             = models.SlugField(max_length=255, unique=True, blank=True, verbose_name='Slug')
    author           = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Auteur')
    category         = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Catégorie')
    last_updated     = models.DateField(blank=True, auto_now=True, null=True, verbose_name='Dernière modification')
    date             = models.DateField(blank=True, auto_now_add=True, null=True, verbose_name='Date de publication')
    resume           = models.CharField(null=True,  blank=True, max_length=255, verbose_name='Résumé')
    content          = EditorJsJSONField(null=True, blank=True, verbose_name='Contenu')
    thumbnail        = models.ImageField(upload_to="thumbnails", blank=True, null=True, verbose_name='Miniature')
    views            = models.IntegerField(default=0, null=True, blank=True, verbose_name="Vues")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-id']

        verbose_name = "Article"
        verbose_name_plural = "Articles"

# Comment Model 

class Comment(models.Model):
    article    = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="Article")
    author     = models.CharField(max_length=255, verbose_name="Auteur")
    content    = models.TextField(verbose_name="Contenu")
    date       = models.DateTimeField(auto_now_add=True, verbose_name="Date")

    class Meta:
        ordering = ["-date"]

        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"