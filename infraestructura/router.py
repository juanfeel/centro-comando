from rest_framework.routers import DefaultRouter
from .views import (
    NodoServidorViewSet,
    RegistroAuditoriaViewSet,
    IncidenciaServidorViewSet
)

router = DefaultRouter()
router.register(r'servidores', NodoServidorViewSet, basename='servidor')
router.register(r'auditorias', RegistroAuditoriaViewSet, basename='auditoria')
router.register(r'incidencias', IncidenciaServidorViewSet, basename='incidencia')

urlpatterns = router.urls