from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
##from django.http import HttpResponse
from .models import Blog, Category, Quote, Quotefield, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'homepage.html')

def BlogsView(request):
    blogs_queryset = Blog.objects.filter(status=1).order_by('-created_on')
    quotes_queryset = Quote.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(blogs_queryset, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    try:
        page = paginator.page(page_number)
    except EmptyPage:   
        page = paginator.page(1)      
    context = {
        'blogs': page,
        'page_obj': page_obj,
        'quotes':  quotes_queryset
    }
    return render(request, 'blogs.html', context)

def DetailView(request, slug):
    blog_post = get_object_or_404(Blog, slug=slug)
    comments = blog_post.comments.filter(active=1).order_by('-created_on')
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog_post = blog_post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'blog': blog_post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form}
    return render(request, 'detail.html', context)

def CategoryView(request, slug):
    category = Category.objects.get(slug=slug)
    category_posts = Blog.objects.filter(status=1, Category = category).order_by('-created_on')
    quotes_queryset = Quote.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(category_posts, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    try:
        page = paginator.page(page_number)
    except EmptyPage:   
        page = paginator.page(1)      
    context = {
        'category':category,
        'category_posts': page,
        'page_obj': page_obj,
        'quotes':  quotes_queryset
    }
    return render(request, 'category.html', context)
