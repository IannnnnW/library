from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'books'
urlpatterns = [
    #Home Page
    path('', views.index, name = 'index'),
    path('home/' ,views.home, name = 'home'),
<<<<<<< HEAD
    path('home/borrow' ,views.borrow, name = 'borrow'),
    path('home/borrow/home2',views.home2),
=======
    path('book/<int:pk>/' ,views.borrow, name = 'book'),
>>>>>>> a9335084cecfeb9b650993021662f234dd60fa0d
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)