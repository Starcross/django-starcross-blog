from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags
from django.utils.timezone import now
from django.urls import reverse
from tinymce.models import HTMLField


class BlogEntry(models.Model):
    title = models.CharField(max_length=250)
    entry_text = HTMLField()
    publication_status = models.CharField(max_length=50, choices=[
        ('draft', 'Draft'),
        ('published', 'Published')
    ], default='draft')
    date_published = models.DateTimeField(default=now)

    @property
    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('blog:blogentry', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blog Entries"


class Comment(models.Model):
    entry = models.ForeignKey(BlogEntry, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    comment_text = HTMLField()

    def __str__(self):
        return strip_tags(self.comment_text[:100])

    def get_absolute_url(self):
        entry_url = reverse('blog:blogentry', kwargs={'pk': self.entry.pk, 'slug': self.entry.slug})
        return f"{entry_url}#comment_{self.pk}"
