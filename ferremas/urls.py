from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .paypal import create_payment,execute_payment,cancel_payment

#API
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)


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
    path('payment/cancel/', cancel_payment, name='cancel_payment'),


    #API
    #API PAGINA
    
    path('productos_api', views.productos_api, name='productos_api'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
