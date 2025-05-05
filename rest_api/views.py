from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from playZoneApp.models import Categoria, Videojuego
from .serializers import CategoriaSerializer, VideojuegoSerializer
import requests
 
# API REST interna
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
 
class VideojuegoViewSet(viewsets.ModelViewSet):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer
 
    @action(detail=False, methods=['get'], url_path=r'categoria/(?P<categoria_id>\d+)')
    def por_categoria(self, request, categoria_id=None):
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            juegos = Videojuego.objects.filter(categoria=categoria)
            serializer = self.get_serializer(juegos, many=True)
            return Response({
                "nombre_categoria": categoria.nombre,
                "videojuegos": serializer.data
            })
        except Categoria.DoesNotExist:
            return Response({"error": "Categoría no encontrada"}, status=404)
 

def api_pokemon(request):
    url = 'https://pokeapi.co/api/v2/pokemon?limit=10'
    response = requests.get(url)
    data = response.json()
    pokemones = data.get('results', [])
    return render(request, 'rest_api/pokemon.html', {'pokemones': pokemones})
 
def api_rickmorty(request):
    url = 'https://rickandmortyapi.com/api/character'
    response = requests.get(url)
    data = response.json()
    personajes = data.get('results', [])
    return render(request, 'rest_api/rickmorty.html', {'personajes': personajes})
 