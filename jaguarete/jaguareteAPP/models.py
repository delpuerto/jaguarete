from django.db import models
from django.db.models.enums import Choices

# Create your models here.

opciones_consultas=[
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]

class Contacto(models.Model):
    nombre        = models.CharField(max_length=50)
    correo        = models.EmailField(null=True)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje       = models.TextField(null=True)
    avisos        = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

