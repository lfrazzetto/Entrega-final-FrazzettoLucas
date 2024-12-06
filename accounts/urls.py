from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Ruta para el registro
    path('login/', views.user_login, name='login'),  # Ruta para el login
    path('logout/', LogoutView.as_view(), name='logout'),  # Ruta para el logout
    path('profile/', views.profile_view, name='profile'),  # Ver profile
    path('profile/edit/', views.edit_profile,
         name='edit_profile'),  # Editar Profile
    path('profile/delete/', views.delete_account,
         name='delete_account'),  # Ruta para eliminar cuenta
]
