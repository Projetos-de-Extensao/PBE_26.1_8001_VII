from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

def home(request):
    return HttpResponse("API de Estágios funcionando!")

schema_view = get_schema_view(
   openapi.Info(
      title="Sistema de Estágios API",
      default_version='v1',
      description="Documentação das rotas app de Estágios",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("estagios.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

