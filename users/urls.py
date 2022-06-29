<<<<<<< HEAD
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'users'
urlpatterns = [
    #login and register Page
    path('login', views.login, name = 'login'),
    path('register/' ,views.register, name = 'register'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register, name='register'),
]
>>>>>>> 7b4eba5f06063ce52231ef6490a40d7cdfee6b7b
