from django.shortcuts import render, redirect
<<<<<<< HEAD
from .forms import registerform
from django.contrib.auth.models import auth
from django.contrib.auth import login as auth_login
=======
<<<<<<< HEAD
from .forms import registerform, LoginForm
from django.contrib.auth.forms import AuthenticationForm
=======
from .forms import registerform
>>>>>>> ee397d61a5124ffb3716fc8d445db0fb1f133743
from django.contrib.auth.models import auth
from django.contrib.auth import login as auth_login

>>>>>>> 0e2bd335e6a14be4d66c45a4b3c0f5c02cf89750
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            return redirect('home')

<<<<<<< HEAD
=======
        user = auth.authenticate(username=Username,password=Password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            pass
<<<<<<< HEAD
=======
>>>>>>> ee397d61a5124ffb3716fc8d445db0fb1f133743
>>>>>>> 0e2bd335e6a14be4d66c45a4b3c0f5c02cf89750
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
