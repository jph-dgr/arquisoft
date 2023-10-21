from ..models import Paciente

def get_pacientes():
    return Paciente.objects.all()

def get_paciente(id):
    return Paciente.objects.get(id=id)

def create_paciente(form_data):
    return Paciente.objects.create(**form_data)

def update_paciente(id, form_data):
    paciente = Paciente.objects.get(id=id)
    for key, value in form_data.items():
        setattr(paciente, key, value)
    paciente.save()
    return paciente

def delete_paciente(id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()

def get_paciente_by_documento(documento):
    try:
        return Paciente.objects.get(documento=documento)
    except Paciente.DoesNotExist:
        return None