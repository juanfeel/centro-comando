from django.urls import path
from .views import lista_servidores, detalle_servidor

urlpatterns = [
    path('', lista_servidores, name='lista_servidores'),
    path('servidor/<int:pk>/',detalle_servidor, name = 'detalle_servidor')
]