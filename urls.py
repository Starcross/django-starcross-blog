from django.urls import path, include

from blog.views import BlogEntryList, BlogEntryView, CommentCreate, CommentList

app_name = 'blog'
urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', BlogEntryList.as_view(template_name='blog/blogentry_all.html'), name='blogentry_list'),
    path('<int:pk>/<slug>/', BlogEntryView.as_view(), name='blogentry'),
    path('comment_create', CommentCreate.as_view(), name='comment_form'),
    path('latest_comments', CommentList.as_view(), name='latest_comments')
]
