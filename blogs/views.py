from django.shortcuts import render
##from django.http import HttpResponse
from .models import blog, Category

def index(request):
    blogs = blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'homepage.html', context)

