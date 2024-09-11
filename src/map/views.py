from django.shortcuts import render, get_object_or_404
from .models import Area

def MapDetailView(request):
    areas = Area.objects.all()
    return render(request, 'map/map.html', { 'areas': areas })