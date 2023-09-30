from django import forms
from .models import HistoriaClinica, Adenda

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'condiciones_cronicas', 'cirugias']

class AdendaForm(forms.ModelForm):
    class Meta:
        model = Adenda
        fields = ['nota', 'autor']




