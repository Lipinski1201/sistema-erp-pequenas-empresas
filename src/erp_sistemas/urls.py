from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes.views import ClienteViewSet

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet, basename="cliente")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # outras rotas…
]
