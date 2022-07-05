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
    path('book/<int:pk>/' ,views.borrow, name = 'book'),
    path('profile/', views.profile, name = 'profile'),
<<<<<<< HEAD
=======
    path('borrowed_book', views.borrowed_book, name = 'borrowed_book'),
    path('returned_book', views.returned_book, name = 'returned_book'),
    path('notifications', views.notifications, name = 'notifications'),
    path('fines', views.fines, name = 'fines'),
>>>>>>> ed1efdddef21eed6a046140558ea252e935c9c78
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)