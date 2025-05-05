from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaViewSet,
    VideojuegoViewSet,
    api_pokemon,
    api_rickmorty
)
 
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'videojuegos', VideojuegoViewSet, basename='videojuego')
 
urlpatterns = [
    path('', include(router.urls)),  # para la API REST
    # para las vistas HTML que consumen APIs externas
    path('pokemon/', api_rickmorty, name='pokemon'),
    path('rickmorty/', api_rickmorty, name='rickmorty'),
]
