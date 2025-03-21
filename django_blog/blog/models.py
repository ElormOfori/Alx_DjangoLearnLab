from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from taggit.managers import TaggableManager

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)  # Many-to-Many Relationship
    tags = TaggableManager()  # Using django-taggit
    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')  # Links to a Post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to a User
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set when comment is created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on edit

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
    
