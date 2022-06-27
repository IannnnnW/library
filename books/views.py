from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request):
    return render(request, 'books/index.html')


def home(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/home.html', context)

def borrow(request, pk):
    return render(request, 'books/borrow.html')