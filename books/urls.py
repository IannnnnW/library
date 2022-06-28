from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'books'
urlpatterns = [
    #Home Page
    path('', views.index, name = 'index'),
    path('home/' ,views.home, name = 'home'),
    path('search_book/' ,views.search_book, name = 'search_book'),
    path('book/<int:pk>/' ,views.borrow, name = 'book'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)