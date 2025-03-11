from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#Every Blog has posts, either text, pictures or videos with Title, body, caption, who create and time created.
class Post(models.Model):
   title = models.CharField(max_length=200) # The Blog post's Tttle text should not exceed 200
   content = models.TextField() #Content should be a text, video or picture
   author = models.ForeignKey(User, on_delete=models.CASCADE) #The post created should be linked to the user
   created_at = models.DateTimeField(auto_now_add=True) #This is the time the Post was created
   updated_at = models.DateTimeField(auto_now=True) #This is the time a post already made is editted.
   published = models.BooleanField(default=False)  # This is to indicate if a post has been published or is still in the draft folder


   def __str__(self):
    return self.title
   

