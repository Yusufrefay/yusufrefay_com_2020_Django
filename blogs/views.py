from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> أزيك يا واد يا حسن</h1>")