# Django Blog Authentication System Documentation

## Overview
This documentation provides a comprehensive guide to setting up and managing the authentication system for the `django_blog` project. The authentication system enables users to register, log in, log out, and manage their profiles securely.

## Features
- User Registration with email and password
- User Login and Logout
- Profile Management (view and edit profile)
- Secure password handling
- CSRF protection for form submissions

---

## 1. Setup Instructions

### 1.1 Prerequisites
Ensure you have the following installed:
- Python (>=3.6)
- Django (>=3.2)
- A virtual environment (recommended)

### 1.2 Install Django (if not already installed)
```sh
pip install django
```

### 1.3 Create a Django Project (if not already created)
```sh
django-admin startproject myproject
cd myproject
```

### 1.4 Create the Blog App
```sh
python manage.py startapp blog
```

### 1.5 Add `blog` to Installed Apps in `settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

---

## 2. Authentication System Implementation

### 2.1 User Model and Forms
Django’s built-in `User` model is used for authentication. A custom user registration form is implemented by extending `UserCreationForm`.

**Create `blog/forms.py`:**
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

---

### 2.2 Authentication Views

**Create `blog/views.py`:**
```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# Profile Management
@login_required
def profile(request):
    return render(request, 'auth/profile.html')
```

---

### 2.3 URL Configuration

**Modify `blog/urls.py`:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
```

---

### 2.4 Creating Authentication Templates

#### **Register Page (`register.html`)**
```html
{% extends "base.html" %}
{% block content %}
<h2>Register</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
</form>
<a href="{% url 'login' %}">Already have an account? Login</a>
{% endblock %}
```

#### **Login Page (`login.html`)**
```html
{% extends "base.html" %}
{% block content %}
<h2>Login</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
<a href="{% url 'register' %}">Don't have an account? Register</a>
{% endblock %}
```

#### **Profile Page (`profile.html`)**
```html
{% extends "base.html" %}
{% block content %}
<h2>Welcome, {{ user.username }}!</h2>
<p>Email: {{ user.email }}</p>
<a href="{% url 'logout' %}">Logout</a>
{% endblock %}
```

---

## 3. Security Measures
- **CSRF Protection:** Included using `{% csrf_token %}` in all forms.
- **Password Hashing:** Django securely hashes passwords using PBKDF2 by default.
- **Login Required for Profile Management:** `@login_required` ensures only authenticated users can access the profile page.

---

## 4. Testing the Authentication System

### 4.1 Running the Server
```sh
python manage.py runserver
```

### 4.2 Testing Features
1. **Registration:** Go to `http://127.0.0.1:8000/register/` and create an account.
2. **Login:** Visit `http://127.0.0.1:8000/login/` and enter your credentials.
3. **Profile Management:** After logging in, navigate to `http://127.0.0.1:8000/profile/`.
4. **Logout:** Click on "Logout" to sign out.

---

## 5. Deployment Considerations
Before deploying, ensure:
- Debug mode is turned off (`DEBUG = False` in `settings.py`).
- A secure secret key is used (`SECRET_KEY`).
- A production-ready database (e.g., PostgreSQL) is configured.

---

## 6. Conclusion
This documentation provides a detailed explanation of how to set up user authentication in Django, including registration, login, logout, and profile management. The system is secure, user-friendly, and customizable to meet additional needs.

For any questions or enhancements, refer to the official [Django documentation](https://docs.djangoproject.com/en/stable/topics/auth/).


# Comment Functionality
Users can:
- Add comments (authenticated users only).
- Edit their own comments.
- Delete their own comments.
- View all comments under a blog post.
Permissions:
- Only authenticated users can comment.
- Only the author of a comment can edit or delete it.
