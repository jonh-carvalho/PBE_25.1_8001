from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'entrevistadores', views.EntrevistadorViewSet)
router.register(r'domicilios', views.DomicilioViewSet)
router.register(r'entrevistas', views.EntrevistaViewSet)
router.register(r'relatorios', views.RelatorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]