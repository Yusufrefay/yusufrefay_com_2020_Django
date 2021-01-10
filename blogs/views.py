from django.shortcuts import render
##from django.http import HttpResponse
from .models import Blog, Category


def index(request):
    return render(request, 'homepage.html')

def blogs(request):
    blogs_queryset = Blog.objects.all()

    context = {
        'blogs': blogs_queryset
    }
    return render(request, 'blogs.html', context)


def detail(request, slug):
    blog_post = Blog.objects.get(slug=slug)
    
    context = {
        'blog': blog_post
    }
    return render(request, 'detail.html', context)