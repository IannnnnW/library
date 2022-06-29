from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'home.html', context)

def borrow(request, pk):
    return render(request, 'borrow.html')


