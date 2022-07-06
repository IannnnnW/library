import profile
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
    path('borrow/' ,views.borrow, name = 'borrow'),
    path('profile/', views.profile, name = 'profile'),
    path('borrowed_book/', views.borrowed_book, name = 'borrowed_book'),
    path('returned_book/', views.returned_book, name = 'returned_book'),
    path('notifications', views.notifications, name = 'notifications'),
<<<<<<< HEAD
    path('fines', views.fines, name = 'fines'),
    path('search_book/confirm_borrow', views.confirm_borrow, name = 'confirm_borrow'),
    
=======
>>>>>>> 6aac15ccd9d65695bf9bfc7ff48ac9cf97f3ccc6
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)