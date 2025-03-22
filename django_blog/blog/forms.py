from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Tag
from .models import Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        return content
    

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas.")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        # Extract tags from form input
        post = super().save(commit=False)
        tag_names = self.cleaned_data['tags'].split(',')  # Convert string to list

        if commit:
            post.save()  # Save post first
            post.tags.clear()  # Remove old tags

            # Add or create new tags
            for tag_name in tag_names:
                tag_name = tag_name.strip()
                if tag_name:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)

        return post
