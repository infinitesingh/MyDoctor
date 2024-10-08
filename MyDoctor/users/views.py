# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

import logging

from django.contrib.auth import get_user_model

User = get_user_model()

logger = logging.getLogger('django')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f"form is %s",user)
            login(request, user)
            messages.success(request, 'Your account has been created! You are now logged in.')
            return redirect('home')

        else:
            logger.info("invalid form")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'signup_form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}.')
                logger.info("Login success")
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
                logger.info("Invalid form")
        else:
            messages.error(request, 'Invalid username or password.')
            logger.info("Invalid cred")
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

def userHomeView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:   
        form = AuthenticationForm()
        return redirect('login')
    
@login_required
def profileView(request):
        return render(request,'users/profile.html')