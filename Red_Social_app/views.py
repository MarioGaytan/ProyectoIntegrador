from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import viewsets
from .serializer import PostSerializer
from .models import Post, APICredential
import random
import string

class MyAuthorizedView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        # Verificar si se proporciona una clave API válida
        api_key = request.query_params.get('api_key')
        if not APICredential.objects.filter(key=api_key).exists():
            return JsonResponse({'error': 'API key invalid'}, status=401)
        
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET'])
def home(request):
    return render(request, "home.html")

def generate_api_key(length=64):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_api_credentials():
    key = generate_api_key()
    api_credential = APICredential.objects.create(key=key)
    return api_credential
