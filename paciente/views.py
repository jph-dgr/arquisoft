from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import PacienteForm
from .logic.paciente_logic import get_pacientes, get_paciente, create_paciente, update_paciente, delete_paciente, get_paciente_by_documento

def paciente_list(request):
    pacientes = get_pacientes()
    context = {'paciente_list': pacientes}
    return render(request, 'Paciente/paciente.html', context)

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            create_paciente(form.cleaned_data)
            messages.success(request, 'Paciente creado correctamente.')
            return redirect(reverse('paciente_list'))
    else:
        form = PacienteForm()
    context = {'form': form}
    return render(request, 'Paciente/pacienteCreate.html', context)

def paciente_edit(request, id):
    paciente = get_paciente(id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            update_paciente(id, form.cleaned_data)
            messages.success(request, 'Paciente actualizado correctamente.')
            return redirect(reverse('paciente_list'))
    else:
        form = PacienteForm(instance=paciente)
    context = {'form': form}
    return render(request, 'Paciente/pacienteCreate.html', context)

def paciente_delete(request, id):
    delete_paciente(id)
    messages.success(request, 'Paciente eliminado correctamente.')
    return redirect(reverse('paciente_list'))

def paciente_search(request):
    paciente = None
    if request.method == 'POST':
        documento = request.POST.get('documento')
        paciente = get_paciente_by_documento(documento)
    context = {'paciente': paciente}
    return render(request, 'Paciente/paciente_search.html', context)
