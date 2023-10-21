from paciente.models import Paciente
from ..models import HistoriaClinica

def get_historias_clinicas():
    return HistoriaClinica.objects.all()

def create_historia_clinica(data):
    condiciones = data.pop('condiciones_cronicas', None)
    cirugias_realizadas = data.pop('cirugias', None)
    
    historia = HistoriaClinica.objects.create(**data)
    
    if condiciones:
        historia.condiciones_cronicas.set(condiciones)
    
    if cirugias_realizadas:
        historia.cirugias.set(cirugias_realizadas)
    
    return historia

def get_historia_clinica_by_id(historia_id):
    return HistoriaClinica.objects.get(id=historia_id)

def get_historia_by_documento(documento):
    try:
        paciente = Paciente.objects.get(documento=documento)
        return HistoriaClinica.objects.get(paciente=paciente)
    except (Paciente.DoesNotExist, HistoriaClinica.DoesNotExist):
        return None



# Agregamos más funciones según las necesidades (actualizar, eliminar, etc.).
