from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
##from django.http import HttpResponse
from .models import Blog, Category

def index(request):
    return render(request, 'homepage.html')

def blogs(request):
    blogs_queryset = Blog.objects.filter(status=1).order_by('-created_on')
    
    paginator = Paginator(blogs_queryset, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    try:
        page = paginator.page(page_number)
    except EmptyPage:   
        page = paginator.page(1)      
    print("Page Number is ")
    print(page_number)
    context = {
        'blogs': page,
        'page_obj': page_obj    
    }
    return render(request, 'blogs.html', context)


def detail(request, slug):
    blog_post = Blog.objects.get(slug=slug)
    
    context = {
        'blog': blog_post
    }
    return render(request, 'detail.html', context)