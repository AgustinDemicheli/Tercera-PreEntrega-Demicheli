
from django.urls import path
from AppSnake import views

urlpatterns= [
            path('',views.inicio,name= 'Inicio'),
            path('cientificos/', views.cientificos,name='Cientificos'),
            path('medicos/',views.medicos,name="Medicos"),
            path('proyecto/',views.proyecto, name='Proyecto'),
            path('medicoFormulario/',views.medicoFormulario, name='medicoFormulario'),
            path('medicoBusqueda/',views.medicoBusqueda, name='medicoBusqueda'),
            path('buscar/',views.buscar),
            path('cientificoFormulario/',views.cientificoFormulario,name='cientificoFormulario'),
            path('cientificoBusqueda/',views.cientificoBusqueda,name='cientificoBusqueda'),
            path('buscar2/',views.buscar2),
            
            ]