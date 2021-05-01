from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField()
    
    class Meta: 
        verbose_name_plural = 'Categories'
   
    def __str__(self):
        return self.title


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    Category = models.ForeignKey(Category, related_name="blog", on_delete= models.CASCADE,null=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField(blank=True, null=True)
    thumb = models.ImageField(default='default.jpg', blank=True, upload_to='Blogs/thumbs/')
    Blog_Background= models.ImageField(default='default.jpg', blank=True, upload_to='Blogs/blog_backgrounds/')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


# Comments Model your models here.
class Comment(models.Model):
    blog_post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

# Quotes Model your models here.

class Quotefield(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField()
    
    class Meta: 
        verbose_name_plural = 'Type'
   
    def __str__(self):
        return self.title


class Quote(models.Model):
    title = models.CharField(max_length=200, unique=True)
    Category = models.ForeignKey(Quotefield, related_name="Quote", on_delete= models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
