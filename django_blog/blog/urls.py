from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, PostByTagListView
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
from .views import search_posts, posts_by_tag


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
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-add"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
    path('search/', search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]
