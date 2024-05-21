from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    
    TIPO_USUARIO_CHOICES = [
                    ('arrendatario', 'Arrendatario'), 
                    ('arrendador', 'Arrendador'),
                            ]     
    rut = models.CharField(max_length=10 , unique=True , null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=10, null=False, blank=False)
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_USUARIO_CHOICES)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Inmueble(models.Model):

    NOMBRE_TIPO_INMUEBLE_CHOICES = [
                        ('casa', 'Casa'),
                        ('departamento', 'Departamento'),
                        ('parcela', 'Parcela'),
    ]   
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    m2_construidos = models.FloatField(null=True, blank=True)
    m2_totales = models.FloatField(null=True, blank=True)
    cantidad_estacionamientos = models.IntegerField(null=True, blank=True)
    cantidad_habitaciones = models.IntegerField(null=True, blank=True)
    cantidad_banos = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=255, unique=True)
    tipo_inmueble = models.CharField(max_length=12, choices=NOMBRE_TIPO_INMUEBLE_CHOICES)
    precio_mensual_arriendo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='propiedades')
        
        
class Area_Geografica(models.Model):
    comuna = models.CharField(max_length=255, unique=True)
        
class SolicitudArriendo(models.Model):
        
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes')
    arrendatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitudes')
    fecha_solicitud = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    estado_solicitud = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')])
        
        