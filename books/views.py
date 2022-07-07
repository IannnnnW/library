from django.shortcuts import render,redirect
from . import models
from .models import Book
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import *
from django.urls import reverse

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
        context = { 'searched':searched,'books':books }

        return render(request, 'books/search_book.html', context)
    else:
        return render(request, 'books/search_book.html')

@login_required
def borrow(request):
    if request.method == "POST":
        # clicked = request.POST['clicked']
        # books = Book.objects.filter(title__icontains=clicked)
        # context = { 'clicked':clicked, 'books':books }
        confirm_borrow(request,1)

        return render(request, 'books/borrow.html')
    else:
        return render(request, 'books/borrow.html')

def get_return_date():
  return datetime.today() + timedelta(days = 14)

def book_time_limit():
  return datetime.now() + timedelta(hours=6)

@login_required
def confirm_borrow(request,id):
    book = Book.objects.get(id=id)
    borrower = Borrower(first_name=request.user.first_name,book_name=book.title,reg_no=request.user.last_name)
    borrower.save()
 
    requested_book = RequestedBook(book_name = book.title,issued_date = datetime.now(),return_date=get_return_date() ,pickup_time = book_time_limit(),borrower=request.user)
    requested_book.save()

    
    return redirect('books:index')



"""Defining views for the profile page"""
@login_required
def profile(request):
    return render(request, 'books/profile.html')


@login_required
def borrowed_book(request):
    requested_book = models.RequestedBook.objects.all()
    li = []
    for book in requested_book:
        issuedate = str(book.issued_date.day)+'-'+str(book.issued_date.month)+'-'+str(book.issued_date.year)
        return_date = str(book.return_date.day)+'-'+str(book.return_date.month)+'-'+str(book.return_date.year)

        books = list(models.Book.objects.filter(book_num = book.book_num))
        students = list(models.Borrower.objects.filter(reg_no = book.reg_no))
        i = 0
        for li in books:
            t = (students[i].get_name, students[i].reg_no, books[i].name, books[i].author, issuedate, return_date)
            i += 1
            li.append(t)
        
    return render(request, 'books/borrowed_book.html')
    

@login_required
def returned_book(request):
    return render(request, 'books/returned_book.html')

@login_required
def notifications(request):
    return render(request, 'books/notifications.html')
@login_required
def fines(request):
    if request.method == 'POST':
        pass


    else:
        pass
    
    return render(request, 'books/fines.html')







