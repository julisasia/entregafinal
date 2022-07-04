from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=80)
    cuerpo = models.CharField(max_length=400)
    fecha_creacion = models.DateField()
    autor = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to ='uploads/', null=True, blank=True)

    

