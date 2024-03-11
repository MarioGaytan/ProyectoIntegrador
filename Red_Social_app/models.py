from django.db import models

class Post(models.Model):
    id_usuario = models.IntegerField()
    usuario = models.CharField(max_length=255)
    fecha_publicacion = models.DateField(auto_now_add=True)
    contenido = models.TextField()
    Imagen = models.ImageField(upload_to='uploads/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.usuario} - {self.fecha_publicacion}'

# Create your models here.
