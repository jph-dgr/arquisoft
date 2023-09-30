from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'fecha_nacimiento', 'telefono', 'email', 'contacto_emergencia', 'telefono_emergencia', 'documento']
