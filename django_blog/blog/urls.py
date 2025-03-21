from django.urls import path
from .views import register_view, login_view, logout_view, profile_view
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView
)



urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path('posts', PostListView.as_view(), name='post-list'),  # Homepage showing all posts
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # View post details
    path("post/new/", PostCreateView.as_view(), name="post-create"),  # Create post
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # Edit post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),  # Delete post
    path("post/<int:pk>/comments/new/", CommentCreateView, name="comment-add"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
