from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request):
    return render(request, 'books/index.html')


def home(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/home.html', context)

def search_book(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__icontains=searched)
        context = {'searched':searched,
                   'books':books }

        return render(request, 'books/search_book.html', context)
    else:
        return render(request, 'books/search_book.html')

def borrow(request, pk):
    return render(request, 'books/borrow.html')

def profile(request):
    return render(request, 'books/profile.html')


