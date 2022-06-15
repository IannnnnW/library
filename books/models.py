from django.db import models
from django.forms import CharField

# Create your models here.
class Book(models.Model):
  CATEGORY = [
    ('education', 'Education'),
    ('entertainment', 'Entertainment'),
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
  name = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  category = models.CharField(max_length=40, choices = CATEGORY)
  status = models.CharField(max_length = 30, choices=STATUS_CHOICES)
  description = models.CharField(max_length=1000)
  image = models.ImageField(upload_to = 'pics')
  class Meta:
    verbose_name_plural = 'books'

  def __str__(self):
    return self.name

