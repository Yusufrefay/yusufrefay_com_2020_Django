from django.shortcuts import render
##from django.http import HttpResponse
from .models import blog, Category

def index(request):
    blogs_queryset = blog.objects.all()

    context = {
        'blogs': blogs_queryset
    }
    return render(request, 'homepage.html', context)

def detail(request, slug):
    blog_post = blog.objects.get(slug=slug)
    
    context = {
        'blog': blog_post
    }
    return render(request, 'detail.html', context)