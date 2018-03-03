from django.db import models
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

class BlogEntry(models.Model):
    title = models.CharField(max_length=250)
    entry_text = HTMLField()
    date_published = models.DateTimeField(default=now)

    @property
    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title


class Comment(models.Model):
    entry = models.ForeignKey(BlogEntry, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    comment_text = HTMLField()

    def __str__(self):
        return self.comment_text