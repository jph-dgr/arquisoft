from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    contacto_emergencia = models.CharField(max_length=200)
    telefono_emergencia = models.CharField(max_length=15)
    documento = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre
