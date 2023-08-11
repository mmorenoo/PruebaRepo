from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes', verbose_name='imagen', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='Descripción')
    estado = models.BooleanField('estado', default= True)
    
    def __str__(self):
        fila = "Titulo: " + self.titulo + ", Descrpcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        # con la siguiente linea de codigo borro la imagen inclusive en el la carpeta que se crea en el proyectp
        self.imagen.storage.delete(self.imagen.name) 
        super().delete()