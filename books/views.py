from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'books/index.html')


def home(request):
    return render(request, 'books/home.html')

def borrow(request):
    return render(request, 'books/borrow.html')