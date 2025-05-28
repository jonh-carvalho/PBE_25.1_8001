from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.openapi import Parameter, TYPE_STRING, IN_HEADER

schema_view = get_schema_view(
    openapi.Info(
        title="Minha API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

token_param = Parameter(
    name='Authorization',
    in_=IN_HEADER,
    description='Token de autenticação. Use o formato: Token <seu_token>',
    type=TYPE_STRING
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('content_app.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    # URLs do Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]