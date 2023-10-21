from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import HistoriaClinicaForm, AdendaForm
from .logic.historia_clinica_logic import get_historias_clinicas, create_historia_clinica, get_historia_clinica_by_id
from .logic.adenda_logic import get_adendas_by_historia, create_adenda
from .models import HistoriaClinica
from django.views.decorators.csrf import csrf_exempt

def historia_clinica_list(request):
    historias = get_historias_clinicas()
    context = {
        'historia_clinica_list': historias
    }
    return render(request, 'HistoriaClinica/historia_clinica.html', context)

@csrf_exempt
def historia_clinica_detail(request, historia_id):
    historia = get_historia_clinica_by_id(historia_id)
    adendas = get_adendas_by_historia(historia_id)

    if request.method == 'POST':
        form = AdendaForm(request.POST)
        if form.is_valid():
            adenda = form.save(commit=False)
            adenda.historia_clinica_id = historia_id
            adenda.save()
            return redirect('historia_clinica_detail', historia_id=historia_id)  # redireccionar a la misma página

    else:
        form = AdendaForm()

    context = {
        'historia': historia,
        'adenda_list': adendas,
        'form': form
    }
    return render(request, 'HistoriaClinica/historia_clinica_detail.html', context)

@csrf_exempt
def historia_clinica_create(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            create_historia_clinica(form.cleaned_data)
            return redirect('historia_clinica_list')
    else:
        form = HistoriaClinicaForm()
    context = {'form': form}
    return render(request, 'HistoriaClinica/historia_clinica_create.html', context)

def adenda_list(request, historia_id):
    adendas = get_adendas_by_historia(historia_id)
    context = {
        'adenda_list': adendas,
        'historia_id': historia_id
    }
    return render(request, 'HistoriaClinica/adenda_list.html', context)

@csrf_exempt
def adenda_create(request, historia_id):
    if request.method == 'POST':
        form = AdendaForm(request.POST)
        if form.is_valid():
            adenda = form.save(commit=False)
            adenda.historia_clinica_id = historia_id
            adenda.save()
            return redirect('adenda_list', historia_id=historia_id)
    else:
        form = AdendaForm()
    context = {'form': form, 'historia_id': historia_id}
    return render(request, 'HistoriaClinica/adenda_create.html', context)

# Agrega más vistas según las necesidades (editar, eliminar, etc.).

