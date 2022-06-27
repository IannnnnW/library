from django.shortcuts import render,redirect
from .models import Book
# Create your views here.
def index(request):
    return render(request, 'books/index.html')


def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html',{'books':books})

def borrow(request):
    return render(request, 'books/borrow.html')

def home2(request):
    return redirect('/')
    # return render(request,'books/home.html')