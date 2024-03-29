from django.contrib import admin
from .models import Post, Author, Tag, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin): 
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "date",)
    list_display = ("title", "author",) 

class CommentsAdmin(admin.ModelAdmin): 
    list_filter = ("author", "creation_date",)
    list_display = ("content", "author",) 

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentsAdmin)