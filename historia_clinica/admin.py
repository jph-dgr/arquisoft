from django.contrib import admin
from .models import HistoriaClinica, Adenda, CondicionCronica, Cirugia

admin.site.register(HistoriaClinica)
admin.site.register(Adenda)
admin.site.register(CondicionCronica)
admin.site.register(Cirugia)
