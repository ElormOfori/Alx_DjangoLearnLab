from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.

# Register user
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile after signup
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

# Login user
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid username or password'})
    return render(request, 'auth/login.html')

# Logout user
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Profile page (Only accessible when logged in)
@login_required
def profile(request):
    return render(request, 'auth/profile.html', {'user': request.user})
