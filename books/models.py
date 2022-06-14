from django.db import models

# Create your models here.
class books(models.Model):
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
