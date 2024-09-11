from django.contrib import admin

from .models import Area

class AreaAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude")
    fields = ["name", "articles", "latitude", "longitude"]


admin.site.register(Area, AreaAdmin)