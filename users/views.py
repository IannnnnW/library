from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST['password']

        user = auth.authenticate(username=Username,password=Password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
    else:
        return render(request,'books/login.html')


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
