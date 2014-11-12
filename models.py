from django.db import models
from datetime import datetime
from tinymce.models import HTMLField

class BlogEntry(models.Model):
    title = models.CharField(max_length=250)
    entry_text = HTMLField()
    date_published = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title


class Comment(models.Model):
    entry  = models.ForeignKey(BlogEntry)
    name = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    comment_text = HTMLField()

    def __str__(self):
        return self.comment_text