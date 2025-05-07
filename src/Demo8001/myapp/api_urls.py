# myapp/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.api import ProdutoViewSet, ProdutosBaratosAPIView

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('', include(router.urls)),
    path('produtos/baratos/', ProdutosBaratosAPIView.as_view(), name='produtos-baratos'),
]