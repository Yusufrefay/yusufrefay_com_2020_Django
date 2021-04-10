from django.contrib import admin
from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)