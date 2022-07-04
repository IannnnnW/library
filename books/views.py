from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'books/index.html')

"""Defining views for the home page"""
@login_required
def home(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/home.html', context)

"""Defining views for the search_book page"""
@login_required
def search_book(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__icontains=searched)
        context = {'searched':searched,'books':books }

        return render(request, 'books/search_book.html', context)
    else:
        return render(request, 'books/search_book.html')

def borrow(request, pk):
    return render(request, 'books/borrow.html')

"""Defining views for the profile page"""
@login_required
def profile(request):
    return render(request, 'books/profile.html')

def borrowed_book(request):
    return render(request, 'books/borrowed_book.html')

def returned_book(request):
    return render(request, 'books/returned_book.html')

def notifications(request):
    return render(request, 'books/notifications.html')

def fines(request):
    return render(request, 'books/fines.html')


