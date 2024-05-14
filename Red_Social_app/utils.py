from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewset, generate_api_key_view

router = DefaultRouter()
router.register(r'muro', PostViewset, basename='muro')

urlpatterns = [
    path('generate-api-key/', generate_api_key_view, name='generate_api_key'),
    path('api/', include(router.urls)),
]