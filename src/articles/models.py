from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# EditorJS
from django_editorjs_fields import EditorJsJSONField 

# Category Model

class Category(models.Model):
    name        = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    thumbnail   = models.ImageField(upload_to="categories", blank=True, null=True)
    slug        = models.SlugField(max_length=255, unique=True, blank=True)

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

        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

# Article Model 

class Article(models.Model):
    title            = models.CharField(max_length=255, unique=True)
    slug             = models.SlugField(max_length=255, unique=True, blank=True)
    author           = models.CharField(max_length=255, blank=True)
    category         = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated     = models.DateField(blank=True, auto_now=True, null=True)
    resume           = models.CharField(max_length=255)
    content          = EditorJsJSONField(null=True, blank=True)
    thumbnail        = models.ImageField(upload_to="thumbnails", blank=True, null=True)

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
