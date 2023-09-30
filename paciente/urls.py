from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.paciente_list, name='paciente_list'),
    path('create/', views.paciente_create, name='paciente_create'),
    path('edit/<int:id>/', views.paciente_edit, name='paciente_edit'),
    path('delete/<int:id>/', views.paciente_delete, name='paciente_delete'),
]
