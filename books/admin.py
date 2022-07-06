from django.contrib import admin
from .models import Book, Borrower, IssuedBook
# Register your models here.
admin.site.register(Book)
admin.site.register(IssuedBook)
admin.site.register(Borrower)
