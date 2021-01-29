from django.urls import path, include

from blog.views import BlogEntryList, BlogEntryView, CommentCreate

app_name = 'blog'
urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    # ex: /blog/
    path('', BlogEntryList.as_view(template_name='blog/blogentry_all.html'), name='blogentry_list'),
    # ex: /blog/5/title
    path('<int:pk>/<slug>/', BlogEntryView.as_view(), name='blogentry'),
    path('comment', CommentCreate.as_view(), name='comment_form')

]
