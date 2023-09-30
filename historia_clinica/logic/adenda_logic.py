from ..models import Adenda

def get_adendas_by_historia(historia_id):
    return Adenda.objects.filter(historia_clinica_id=historia_id)

def create_adenda(data):
    adenda = Adenda.objects.create(**data)
    return adenda
