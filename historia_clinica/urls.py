from django.urls import path
from . import views

urlpatterns = [
    path('', views.historia_clinica_list, name='historia_clinica_list'),
    path('create/', views.historia_clinica_create, name='historia_clinica_create'),
    path('<int:historia_id>/', views.historia_clinica_detail, name='historia_clinica_detail'),
    path('<int:historia_id>/adendas/', views.adenda_list, name='adenda_list'),
    path('<int:historia_id>/adendas/create/', views.adenda_create, name='adenda_create'),
    # Agrega más patrones de URL según las necesidades (editar, eliminar, etc.).
]
