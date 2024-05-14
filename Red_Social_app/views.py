from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializer import PostSerializer
from .models import Post, APICredential
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey
from django.conf import settings

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [HasAPIKey]

    def get_queryset(self):
        return super().get_queryset()

    def perform_create(self, serializer):
        authorization_header = self.request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            try:
                api_key_value = authorization_header.split()[1]
                api_key = APIKey.objects.get_from_key(api_key_value)
                serializer.save(api_key=api_key_value)  # Guarda el valor de la clave directamente
                print("Post creado con API Key:")
            except APIKey.DoesNotExist:
                print("API Key no válida")
                return JsonResponse({'error': 'Invalid API key'}, status=401)
        else:
            print("Falta la cabecera de autorización")
            return JsonResponse({'error': 'Authorization header is missing'}, status=401)

@api_view(['GET'])
def generate_api_key_view(request):
    api_key = request.headers.get('API-Key')
    if (api_key != settings.MASTER_API_KEY):
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    api_key_instance, key = APIKey.objects.create_key(name="my-remote-service")
    return JsonResponse({'api_key': key})
