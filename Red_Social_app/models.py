from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    PRIVACIDAD_OPCIONES = [
        ('PUB', 'Público'),
        ('CON', 'Solo contactos'),
    ]
    ETIQUETA_OPCIONES = [
        ('CONV', 'Convivencia'),
        ('ACAD', 'Académico'),
        ('AYUD', 'Ayuda/Orientación'),
        ('EMPL', 'Empleos'),
    ]
    
    id_usuario = models.IntegerField()
    usuario = models.CharField(max_length=255)
    fecha_publicacion = models.DateField(auto_now_add=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='uploads/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)  # Refiriéndose al modelo User
    privacidad = models.CharField(max_length=4, choices=PRIVACIDAD_OPCIONES, default='PUB')
    etiqueta = models.CharField(max_length=5, choices=ETIQUETA_OPCIONES, blank=True, null=True)
    
    def __str__(self):
        return f'{self.usuario} - {self.fecha_publicacion}'


class APICredential(models.Model):
    key = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.key} - '
# Create your models here.
