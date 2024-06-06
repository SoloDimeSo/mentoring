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
    correo_electronico = models.EmailField(unique=True, default='correo@correo.cl', null=False, blank=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Region(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Inmueble(models.Model):

    NOMBRE_TIPO_INMUEBLE_CHOICES = [
                        ('casa', 'Casa'),
                        ('departamento', 'Departamento'),
                        ('parcela', 'Parcela'),
    ]   
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    imagen  = models.ImageField(upload_to='inmuebles', null=True, blank=True,)
    imagen_2  = models.ImageField(upload_to='inmuebles', null=True, blank=True,)
    imagen_3  = models.ImageField(upload_to='inmuebles', null=True, blank=True,)
    precio_mensual_arriendo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='inmuebles')
    disponibilidad = models.BooleanField(default=True)
    m2_construidos = models.FloatField(null=True, blank=True)
    m2_totales = models.FloatField(null=True, blank=True)
    cantidad_estacionamientos = models.IntegerField(null=True, blank=True)
    cantidad_habitaciones = models.IntegerField(null=True, blank=True)
    cantidad_banos = models.IntegerField(null=True, blank=True)
    tipo_inmueble = models.CharField(max_length=12, choices=NOMBRE_TIPO_INMUEBLE_CHOICES)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='propiedades')
        
    def __str__(self):
        return self.nombre
        
class SolicitudArriendo(models.Model):
    TIPO_ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    ]
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes')
    arrendatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitudes')
    fecha_solicitud = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    estado_solicitud = models.CharField(max_length=50, choices=TIPO_ESTADO_CHOICES)
    mensaje = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Solicitud de {self.inmueble.nombre} por {self.arrendatario.nombre} {self.arrendatario.apellido}'
        