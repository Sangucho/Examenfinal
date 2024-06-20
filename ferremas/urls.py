from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .paypal import create_payment,execute_payment,cancel_payment

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('signin/', views.signin, name='signin'),
    path('agregarproducto/', views.agregarproducto, name='agregarproducto'),
    path('editarproducto/',views.editarproducto, name='editarproducto'),
    path('perfilusuario/',views.editarproducto, name='perfilusuario'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    path('carrito/', views.carrito, name='carrito'),
    path('payment/create/', create_payment, name='create_payment'),
    path('payment/execute/', execute_payment, name='execute_payment'),
    path('payment/cancel/', cancel_payment, name='cancel_payment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
