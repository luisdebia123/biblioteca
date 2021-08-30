from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import timedelta

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombres',max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos',max_length=220, blank=False, null=False)
    nacionalidad = models.CharField('Nacionalidad',max_length=100, blank=False, null=False)
    descripcion =models.TextField('Descripción',blank=False, null=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)
    

    class Meta:
        verbose_name ='Autor'
        verbose_name_plural ='Autores'
        ordering = ['id']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de publicacion', blank=False, null=False)
    descripcion = models.TextField('Descripción', null=True, blank=True)
    cantidad = models.PositiveIntegerField('Cantidad', default=1)
    imagen = models.ImageField('imagen', upload_to='libros', max_length =255, blank=True, null=True) 
    autor_id = models.ManyToManyField(Autor, related_name='autor')
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)
    estado = models.BooleanField(default =True, verbose_name='Estado')
    

    class Meta:
        verbose_name ='Libro'
        verbose_name_plural ='Libros'
        ordering =['id']

    def __str__(self):
        return self.titulo

    def obtener_autores(self):
        autores = str([autor for autor in self.autor_id.all().values_list('nombre', flat=True)]).replace('[','').replace(']','').replace("'",'')
        return autores


'''
    def obtener_autores(self):
        autores = self.autor_id.all().values_list('nombre', flat=True)
        return autores
'''


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad_dias = models.SmallIntegerField('Cantidad de días a Reservar', default=7)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_vencimiento = models.DateField('Fecha de vencimiento',auto_now=False,auto_now_add =False,null=True,blank=True)
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'Reserva de Libro {self.libro} por {self.usuario}'

    def save(self, *args, **kwargs):
        self.fecha_vencimiento = self.fecha_creacion + timedelta(days=self.cantidad_dias)
        super().save(*args, **kwargs)

