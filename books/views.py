<<<<<<< HEAD
from django.shortcuts import render,redirect
=======
from django.shortcuts import render
>>>>>>> a9335084cecfeb9b650993021662f234dd60fa0d
from .models import Book
# Create your views here.
def index(request):
    return render(request, 'books/index.html')


def home(request):
    books = Book.objects.all()
<<<<<<< HEAD
    return render(request, 'books/home.html',{'books':books})

def borrow(request):
    return render(request, 'books/borrow.html')

def home2(request):
    return redirect('/')
    # return render(request,'books/home.html')
=======
    context = {'books':books}
    return render(request, 'books/home.html', context)

def borrow(request, pk):
    return render(request, 'books/borrow.html')
>>>>>>> a9335084cecfeb9b650993021662f234dd60fa0d
