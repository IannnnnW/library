from django.contrib import admin
<<<<<<< HEAD
from .models import *
# Register your models here.
admin.site.register([Book,IssuedBook,Borrower])
=======
from .models import Book, Borrower, IssuedBook
# Register your models here.
admin.site.register(Book)
admin.site.register(IssuedBook)
admin.site.register(Borrower)
>>>>>>> 6aac15ccd9d65695bf9bfc7ff48ac9cf97f3ccc6
