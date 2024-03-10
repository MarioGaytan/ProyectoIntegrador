from django.shortcuts import render
from .serializer import PostSerializer
from .models import Post
from rest_framework import viewsets

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def home(request):
    return render(request, "home.html")

