from django.shortcuts import render
##from django.http import HttpResponse
from .models import blog, Category

def index(request):
    blogs = blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'homepage.html', context)

def detail(request, slug):
    blogs = blog.objects.get(slug=slug)
    
    context = {
        'blogs': blogs
    }
    # leeh dah me4 48al
    """  blog = blog.objects.get(slug=slug)
    
    context = {
        'blog': blog
    } """
    return render(request, 'detail.html', context)