from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Leer blogs
    path('about/', views.about, name='about'),  # Página "Acerca de mí"
    path('blog/<int:blog_id>/', views.blog_detail,
         name='blog_detail'),  # Ver detalle del blog
    path('blog/new/', views.blog_create,
         name='blog_create'),  # Crear un nuevo blog
    path('blog/<int:blog_id>/edit/', views.blog_update,
         name='blog_update'),  # Editar un blog
    path('blog/<int:blog_id>/delete/', views.blog_delete,
         name='blog_delete'),  # Borrar un blog
]
