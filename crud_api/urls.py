"""
URL configuration for crud_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Red_Social_app import views
from rest_framework import routers
from Red_Social_app.views import generate_api_key_view
router = routers.DefaultRouter()
router.register('muro',views.PostViewset)

urlpatterns = [
    path('mangofriends/', admin.site.urls),
    path('api/', include(router.urls)),
    path('generate-api-key/', generate_api_key_view, name='generate_api_key')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
