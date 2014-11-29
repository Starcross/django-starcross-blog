from django.contrib import admin
from blog.models import BlogEntry, Comment

# Blog
admin.site.register(BlogEntry)
admin.site.register(Comment)
