from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('signin/', views.signin, name='signin'),
    path('agregarproducto/', views.agregarproducto, name='agregarproducto'),
    path('editarproducto/',views.editarproducto, name='editarproducto'),
    path('perfilusuario/',views.editarproducto, name='perfilusuario'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
     path('process_payment/', views.process_payment, name='process_payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('payment/create/', views.payment_create, name='payment_create'),
    path('payment/execute/', views.payment_execute, name='payment_execute'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
    path('payment/error/', views.payment_error, name='payment_error'),
]
