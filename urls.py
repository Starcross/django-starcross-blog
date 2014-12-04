from django.conf.urls import patterns, url

from blog.views import BlogEntryList, BlogEntryView, CommentCreate

urlpatterns = patterns('',
    # ex: /blog/
    url(r'^$', BlogEntryList.as_view(template_name='blog/blogentry_all.html'),name='blogentry_list'),
    # ex: /blog/5/
    url(r'^(?P<pk>\d+)/$', BlogEntryView.as_view(), name='blogentry'),
    url(r'^comment$', CommentCreate.as_view(), name='comment_form'),

)