from django.db import models
from django.conf import settings
from django.utils import timezone

class Pintor(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='artistas/', blank=True, null=True) 
    biografia = models.TextField()
    nacionalidad = models.CharField(max_length=20)
    tiempo_activo = models.IntegerField(null=True, blank=True)
    cantidad_de_obras = models.IntegerField(null=True, blank=True)
    obra_destacada = models.CharField(max_length=100)
    imagen2 = models.ImageField(upload_to='artistas/', blank=True, null=True) 
    informacion_adicional = models.TextField(blank=True, null=True)
    tecnica_utilizada= models.CharField(max_length=100)
    movimiento = models.CharField(max_length=100)
    acerca_del_movimiento = models.TextField()
    paleta_utilizada = models.CharField(max_length=100)
    imagen3 = models.ImageField(upload_to='artistas/', blank=True, null=True) 
    
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre