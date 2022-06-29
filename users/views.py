from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
<<<<<<< HEAD
def login(request):
    return render(request, 'login.html')
    
=======

def login(request):
    return render(request,'books/login.html')


>>>>>>> 6abcc2639fd4bcb4e6b8ad1387db177e3a37c76d
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('books:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
