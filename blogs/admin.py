from django.contrib import admin
from .models import Category, Blog, Quote, Quotefield, Comment, Photographer

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','Category', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['Publish_blog', 'Draft_blog']

    def Publish_blog(self, request, queryset):
        queryset.update(status=True)
    
    def Draft_blog(self, request, queryset):
        queryset.update(status=False)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog_post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments', 'hide_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    
    def hide_comments(self, request, queryset):
        queryset.update(active=False)

admin.site.register(Quote)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Quotefield)
admin.site.register(Category)
admin.site.register(Photographer)
