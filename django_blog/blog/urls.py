from django.urls import path
from .views import register_view, login_view, logout_view, profile_view
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)



urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path('', PostListView.as_view(), name='post-list'),  # Homepage showing all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View post details
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create post
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post-edit'),  # Edit post
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),  # Delete post
]
