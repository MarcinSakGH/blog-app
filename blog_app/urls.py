from django.urls import path

from .views import (BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView,
                    BlogDeleteView)

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('post/new/', BlogCreateView.as_view(), name='post-new'),
    path('post/edit/<int:pk>/', BlogUpdateView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', BlogDeleteView.as_view(), name='post-delete'),
]