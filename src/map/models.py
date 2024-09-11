from django.db import models
from django.template.defaultfilters import slugify
from articles.models import Article

class Area (models.Model):

    name             = models.CharField(max_length=255, unique=True, verbose_name='Nom')

    latitude  = models.FloatField(default=0, null=True, blank=True, verbose_name="Latitude")
    longitude = models.FloatField(default=0, null=True, blank=True, verbose_name="Longitude")

    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

        verbose_name = "Zone"
        verbose_name_plural = "Zones"
