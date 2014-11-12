from django.contrib import admin
from blog.models import BlogEntry, Comment
from gallery.models import Image, Album, Tag
from goingout.models import Venue

# Blog
admin.site.register(BlogEntry)
admin.site.register(Comment)
# Gallery
admin.site.register(Image)
admin.site.register(Album)
admin.site.register(Tag)
# Goingout
#admin.site.register(Venue)