from django.db import models
from django.forms import CharField
from datetime import *
# Create your models here.
"""Model that stores the library books"""
class Book(models.Model):
  CATEGORY = [
    ('education', 'Education'),
    ('comics', 'Comics'),
    ('biography', 'Biography'),
    ('history', 'History'),
    ('novel', 'Novel'),
    ('fantasy', 'Fantasy'),
    ('thriller', 'Thriller'),
    ('romance', 'Romance'),
    ('scifi','Sci-Fi')
  ]
  STATUS_CHOICES = [
    ('available', 'Available'),
    ('unavailable', 'Unavailable')
  ]
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  category = models.CharField(max_length=40, choices = CATEGORY)
  status = models.CharField(max_length = 30, choices=STATUS_CHOICES)
  description = models.TextField(max_length=3000)
  image = models.ImageField(upload_to = 'pics', blank = True)
  class Meta:
    verbose_name_plural = 'books'

  def __str__(self):
    return self.title

"""Model for the Users borrowing books"""
class Borrower(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  book_num = models.ForeignKey(Book, on_delete=models.CASCADE)
  reg_no = models.CharField(max_length=20)
  class Meta:
    verbose_name_plural = 'borrowers'

  def __str__(self):
    return str(self.first_name)+"["+str(self.book_num)+']'

"""Function to define the return date of the book"""
def get_return_date():
  return datetime.today() + timedelta(days = 14)

"""Function to define the amount of time for the user to pick the book"""
def book_time_limit():
  return datetime.now() + timedelta(hours=6)

"""Model for the books issued to a borrower"""
class IssuedBook(models.Model):
  book_num = models.ForeignKey(Book, on_delete=models.CASCADE)
  issued_date = models.DateField(auto_now = True)
  return_date = models.DateField(default=get_return_date)
  pickup_time = models.DateTimeField(default=book_time_limit)
  class Meta:
    verbose_name_plural = 'issuedbooks'

  def __str__(self):
    return self.book_num
