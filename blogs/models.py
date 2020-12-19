from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

class blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    Category = models.ForeignKey(Category, related_name="blog", on_delete= models.CASCADE,null=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    thumb = models.ImageField(default='default.jpg', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

