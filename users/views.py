from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    return render(request,'books/login.html')


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            register(request, new_user)
            return redirect('books:login')

    context = {'form': form}
    return render(request, 'books/register.html', context)
