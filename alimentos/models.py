# Create your models here.
from django.db import models


# Create your models here.

class Persona(models.Model):
    id_persona = models.AutoField(db_column='id_persona', primary_key=True)
    rut = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellidos = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=10, blank=True, null=True)
    cargo = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    tipo = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.rut + " -- " + self.nombre + " -- " + self.apellidos \
            + " -- " + self.email + " -- " + self.direccion + " -- " + self.cargo + " -- " + self.comuna \
            + "," + self.telefono + " -- " + self.tipo