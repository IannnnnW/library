from django.shortcuts import render, redirect
from .forms import registerform
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
        form = registerform()

    else:
        form = registerform(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            register(request, new_user)
        return redirect('/login')

    context = {'form': form}
    return render(request, 'books/register.html', context)
