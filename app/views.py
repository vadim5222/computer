from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm, RegisterForm
from django.contrib import auth
from django.contrib.auth import logout



def home(request):
    return render(request, "home.html")



def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


