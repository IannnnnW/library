from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users.forms import LoginForm
from . import views
from django.contrib.auth.views import LoginView
app_name = 'users'
urlpatterns = [
    #login and register Page
<<<<<<< HEAD
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
=======
    path('login/', LoginView.as_view(authentication_form = LoginForm), name = 'login'),
    path("register/", views.register, name = 'register'),
>>>>>>> 0e2bd335e6a14be4d66c45a4b3c0f5c02cf89750
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
