from django.core.urlresolvers import reverse
from django.forms import ModelForm, HiddenInput
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from captcha.fields import CaptchaField

from blog.models import BlogEntry, Comment

class BlogEntryList(ListView):
    model = BlogEntry

class BlogEntryView(DetailView):
    model = BlogEntry

    def get_context_data(self, **kwargs):
        context = super(BlogEntryView, self).get_context_data(**kwargs)
        comment_form = CommentCreateForm()
        context['comment_form'] = comment_form
        return context

class CommentCreateForm(ModelForm):

    captcha = CaptchaField()
    class Meta:
        model = Comment
        widgets = {'entry' : HiddenInput()}
    class Media:
        css = {
            'all' : ('highlight/styles/dark.css',)
        }
        js = ('highlight/highlight.pack.js',)

class CommentCreate(CreateView):
    model = Comment
    form_class = CommentCreateForm

    def get_success_url(self):
        return reverse('blog:blogentry', kwargs={'pk': self.object.entry.pk})


