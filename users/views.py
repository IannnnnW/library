from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
<<<<<<< HEAD

def login(request):
    return render(request,'login.html')

def register(request):
    pass
=======
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
>>>>>>> 7b4eba5f06063ce52231ef6490a40d7cdfee6b7b
