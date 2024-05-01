from django.shortcuts import render
from .serializer import PostSerializer
from .models import Post
from rest_framework import viewsets
from rest_framework_api_key.permissions import HasAPIKey
from django.http import JsonResponse
from .utils import create_api_key
from rest_framework_api_key.models import APIKey
from django.conf import settings
# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [HasAPIKey]
    def get_queryset(self):
        return super().get_queryset()

    def perform_create(self, serializer):
        authorization_header = self.request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            api_key_value = authorization_header.split()[1]
            api_key = APIKey.objects.get_from_key(api_key_value)
            serializer.save(api_key=api_key)
        else:
            return JsonResponse({'error': 'Authorization header is missing'}, status=401)

def home(request):
    return render(request, "home.html")



def generate_api_key_view(request):
    # Verifica si se proporciona una llave API válida en el encabezado de la solicitud
    api_key = request.headers.get('API-Key')

    # Verifica si la llave API proporcionada coincide con la llave API maestra
    if api_key != settings.MASTER_API_KEY:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    # Si la llave API es válida, genera una nueva llave API
    api_key_instance, key = APIKey.objects.create_key(name="my-remote-service")
    return JsonResponse({'api_key': key})