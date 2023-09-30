from django.db import models
from paciente.models import Paciente
from django.contrib.auth.models import User

class CondicionCronica(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre

class Cirugia(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre

class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, related_name="historia_clinica")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    condiciones_cronicas = models.ManyToManyField(CondicionCronica, blank=True)
    cirugias = models.ManyToManyField(Cirugia, blank=True)

    def __str__(self):
        return f"Historia Clínica de {self.paciente.nombre}"

class Adenda(models.Model):
    historia_clinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, related_name="adendas")
    fecha = models.DateTimeField(auto_now_add=True)
    nota = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Adenda de {self.fecha} por {self.autor}"
