from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'users'
urlpatterns = [
<<<<<<< HEAD
    #path('',include('django.contrib.auth.urls')),
    path('login', views.login, name= 'login'),
    path('register/',views.register, name='register'),
]
=======
    #login and register Page
    path('login', views.login, name = 'login'),
    path('register/' ,views.register, name = 'register'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 6abcc2639fd4bcb4e6b8ad1387db177e3a37c76d
