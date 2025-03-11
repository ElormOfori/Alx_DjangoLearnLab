from django.shortcuts import render, get_object_or_404 #Render is used to display an HTML Page
from .models import Post # This is where the Blog Posts is be stored in the database

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at') # This is to get all Posts published
    return render(request, 'blog/post_list.html', {'posts': posts}) # This shows all post list once it is clicked


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id) #This is to find the post with the specified ID
    return render(request, 'blog/post_detail.html', {'post': post}) #Show the Blog Post detail page and post to HTML so it can display it
