# Introdução ao Django REST

Uma extensão do aplicativo Django inicial para incluir uma API RESTful usando Django REST Framework, mantendo a funcionalidade existente e adicionando endpoints API.

## 1. Instalação e Configuração Inicial

Primeiro, vamos instalar e configurar o DRF:

```bash
pip install djangorestframework
```

Adicione ao `INSTALLED_APPS` em `myproject/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapp',
]
```

## 2. Criação dos Serializers

Crie um arquivo `serializers.py` na aplicação `minhaapp`:

```python
# minhaapp/serializers.py
from rest_framework import serializers
from myapp.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'descricao', 'disponivel']
        read_only_fields = ['id']
```

## 3. Criação das Viewsets e API Views

Atualize ou crie um arquivo `api.py` na aplicação:

```python
# minhaapp/api.py
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from myapp.models import Produto
from myapp.serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        produtos = Produto.objects.filter(disponivel=True)
        serializer = self.get_serializer(produtos, many=True)
        return Response(serializer.data)

class ProdutosBaratosAPIView(generics.ListAPIView):
    serializer_class = ProdutoSerializer
    
    def get_queryset(self):
        return Produto.objects.filter(preco__lt=1000)
```

## 4. Configuração das URLs da API

Crie um arquivo `api_urls.py` na aplicação:

```python
# myapp/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from minhaapp.api import ProdutoViewSet, ProdutosBaratosAPIView

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('', include(router.urls)),
    path('produtos/baratos/', ProdutosBaratosAPIView.as_view(), name='produtos-baratos'),
]
```

Atualize o `urls.py` principal do projeto:

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # URLs tradicionais
    path('api/', include('minhaapp.api_urls')),  # URLs da API
    path('api-auth/', include('rest_framework.urls')),  # Login para a API
]
```

## 5. Documentação da API com Swagger/OpenAPI

Instale o drf-yasg para documentação:

```bash
pip install drf-yasg
```

Adicione ao `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'drf_yasg',
]
```

Atualize o `urls.py` principal:

```python
# myproject/urls.py
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API de Produtos",
      default_version='v1',
      description="API para gerenciamento de produtos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@empresa.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # ... URLs existentes
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

## 6. Testando a API

Agora você pode testar os endpoints da API:

1. **Listar todos os produtos**: `GET /api/produtos/`
2. **Criar novo produto**: `POST /api/produtos/`
3. **Detalhes de um produto**: `GET /api/produtos/1/`
4. **Atualizar produto**: `PUT /api/produtos/1/`
5. **Produtos disponíveis**: `GET /api/produtos/disponiveis/`
6. **Produtos baratos**: `GET /api/produtos/baratos/`
7. **Documentação Swagger**: `GET /swagger/`
8. **Documentação ReDoc**: `GET /redoc/`

Esta extensão transforma seu aplicativo Django em uma API RESTful poderosa enquanto mantém a funcionalidade web tradicional. Você agora pode:

- Consumir a API com frontends modernos (React, Vue, Angular)
- Oferecer serviços para aplicativos móveis
- Integrar com outros sistemas via API
- Manter uma arquitetura escalável e bem organizada
