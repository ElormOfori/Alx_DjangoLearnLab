#Social Media API

##roject Overview
This project is a basic Social Media API built with Django and Django REST Framework. It includes user authentication, user profiles, posts, and comments with token-based authentication.

#Features
- User Registration
- User Login with Token Authentication
- User Profile Management
- Create, Read, Update, and Delete (CRUD) Posts
- Create, Read, Update, and Delete (CRUD) Comments

#Tech Stack
- Django
- Django REST Framework
- Token Authentication
- SQLite (Default Database)

#Setup Instructions

#Install Dependencies

pip install django djangorestframework djangorestframework-authtoken
```

# Create a Django Project

python3 -m django startproject social_media_api
cd social_media_api
```

#Create Django Apps

Create Django Apps

python manage.py startapp accounts
python manage.py startapp posts

Update settings.py

Add the following to INSTALLED_APPS:

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'posts',
]

Configure Custom User Model

In accounts/models.py:

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

Create Post and Comment Models

In posts/models.py:

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

Apply Migrations

python manage.py makemigrations accounts posts
python manage.py migrate

Create Superuser

python manage.py createsuperuser

Configure URLs

Update social_media_api/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('posts.urls')),
]

API Endpoints

User Authentication

Register: POST /api/register/

Login: POST /api/login/

Profile: GET /api/profile/ (requires authentication)

Posts

Create Post: POST /api/posts/

View Posts: GET /api/posts/

Update Post: PUT /api/posts/{id}/

Delete Post: DELETE /api/posts/{id}/

Comments

Create Comment: POST /api/posts/{id}/comments/

View Comments: GET /api/posts/{id}/comments/

Update Comment: PUT /api/comments/{id}/

Delete Comment: DELETE /api/comments/{id}/

Running the Server

python manage.py runserver

