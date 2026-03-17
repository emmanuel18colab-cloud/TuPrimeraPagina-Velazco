from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('posts/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('posts/nuevo/', views.crear_post, name='crear_post'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/nuevo/', views.crear_autor, name='crear_autor'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('buscar/', views.buscar, name='buscar'),
]