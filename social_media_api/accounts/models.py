from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='follower_users')
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers_users', blank=True
    )

    def follow(self, user):
        #Follow another user
        self.following.add(user)

    def unfollow(self, user):
        #Unfollow a user
        self.following.remove(user)

    def __str__(self):
        return self.username
