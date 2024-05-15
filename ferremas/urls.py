from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicioAdmin/', views.inicioAdmin, name='inicioAdmin'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('agregarproducto/', views.agregarproducto, name='agregarproducto'),
    path('editarproducto/',views.editarproducto, name='editarproducto'),
    path('perfilusuario/',views.editarproducto, name='perfilusuario'),
]
