from .models import Category

def NavProcessor(request):
    return { 'categories': Category.objects.all() }