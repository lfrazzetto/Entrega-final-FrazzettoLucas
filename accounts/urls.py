from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Ruta para el registro
    path('login/', views.user_login, name='login'),  # Ruta para el login
    path('logout/', LogoutView.as_view(), name='logout'),  # Ruta para el logout
]
