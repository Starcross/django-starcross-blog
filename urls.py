from django.urls import path

from blog.views import BlogEntryList, BlogEntryView, CommentCreate

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', BlogEntryList.as_view(template_name='blog/blogentry_all.html'), name='blogentry_list'),
    # ex: /blog/5/
    path('<int:pk>/', BlogEntryView.as_view(), name='blogentry'),
    path('comment', CommentCreate.as_view(), name='comment_form')

]
