from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django.db.models import Q

# Extend UserCreationForm to include email
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# Registration view
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
        else:
            messages.error(request, "Error registering. Check form inputs.")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect("login")

# Profile view (requires login)
@login_required
def profile_view(request):
    if request.method == "POST":
        request.user.email = request.POST["email"]
        request.user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")
    return render(request, "auth/profile.html")


# Display all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template for listing posts
    context_object_name = 'posts'
    ordering = ['-created_at']  # Show newest posts first

# View a single blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template for post details

# Create a new blog post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'  # Template for creating a post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author as the logged-in user
        return super().form_valid(form)

# Edit an existing post (only author can edit)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  # Reuse post form template
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only the author to edit

# Delete a post (only author can delete)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # Template for delete confirmation
    success_url = reverse_lazy('post-list')  # Redirect after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only the author to delete
    
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.id)  # Redirect to post detail page
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})  

#Comment Views

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to logged-in user
        form.instance.post_id = self.kwargs['post_id']  # Get post from URL
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})  # Redirect to post
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only author can edit
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})  # Redirect after deletion

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only author can delete
    
def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(tags__name__icontains=query)  # Search in tags
        ).distinct()

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name=tag_name)
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag_name': tag_name})
