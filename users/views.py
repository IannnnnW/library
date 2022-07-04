from django.shortcuts import render, redirect
from .forms import registerform, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth
from django.contrib.auth import login as auth_login

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            return redirect('home')

    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'registration/login.html', context)


def register(request):
    if request.method != 'POST':
        form = registerform()

    else:
        form = registerform(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request, new_user)
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
