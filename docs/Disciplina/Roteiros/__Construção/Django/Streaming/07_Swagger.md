# 07 - Swagger

## Introdução ao Swagger

Para adicionar o Swagger ao seu projeto Django com Django REST Framework, você pode usar a biblioteca **drf-yasg** (Yet Another Swagger Generator). Esta biblioteca fornece uma interface Swagger para documentar e testar sua API REST.

### Passos para Configurar o Swagger com `drf-yasg`

1. **Instalar o `drf-yasg`**

   Execute o seguinte comando para instalar a biblioteca `drf-yasg`:

   ```bash
   pip install drf-yasg
   ```

2. **Configurar o `drf-yasg` no Projeto**

   Abra o arquivo `urls.py` do seu projeto Django (geralmente o `urls.py` no diretório principal do projeto) e adicione as seguintes configurações para incluir a documentação Swagger.

   ```python
   #streaming_platform/urls.py
   from django.urls import path, re_path
   from rest_framework import permissions
   from drf_yasg.views import get_schema_view
   from drf_yasg import openapi

   # Configuração do Swagger
   schema_view = get_schema_view(
       openapi.Info(
           title="API de Conteúdos",
           default_version='v1',
           description="Documentação da API para o app de streaming de áudio e vídeo",
           terms_of_service="https://www.google.com/policies/terms/",
           contact=openapi.Contact(email="suporte@exemplo.com"),
           license=openapi.License(name="Licença BSD"),
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )

   urlpatterns = [
       # Suas outras URLs
       path('admin/', admin.site.urls),
       path('api/', include('app.urls')),  # Inclua as URLs do seu app

       # URLs do Swagger
       re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
       re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ]
   ```

3. **Acessar a Documentação Swagger e ReDoc**

   Com a configuração acima, você terá acesso a dois tipos de documentação:

   * **Swagger UI**: Interface de documentação interativa. Acesse em:

     ```plaintext
     http://localhost:8000/swagger/
     ```

   * **ReDoc**: Alternativa ao Swagger com uma interface de documentação mais moderna. Acesse em:

     ```plaintext
     http://localhost:8000/redoc/
     ```

4. **Testar a Documentação**

   Ao acessar `http://localhost:8000/swagger/`, você verá a documentação de sua API com base nas views definidas e nos parâmetros dos serializadores. A partir do Swagger, você também pode testar diretamente as endpoints da sua API, enviando requisições com diferentes parâmetros.

### Configuração Opcional

Para personalizar ainda mais o Swagger, você pode ajustar o `schema_view` no arquivo `urls.py` adicionando mais informações ou incluindo permissões específicas.

---

Esses passos devem ser suficientes para configurar e visualizar o Swagger em seu projeto Django, facilitando o uso e a documentação da sua API.
