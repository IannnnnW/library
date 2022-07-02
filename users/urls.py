from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'users'
urlpatterns = [
    #login and register Page
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
