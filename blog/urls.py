from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_homepage'),
    path('view_blog/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    path('add_blog/', BlogCreateView.as_view(), name='add_blog'),
    path('update_blog/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete_blog/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog')
]
