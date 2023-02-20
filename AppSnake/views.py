from django.shortcuts import render
from django.http import HttpResponse
from AppSnake.models import *

#from django.http import HttpResponse
from AppSnake.forms import form_medicos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def inicio(request):
    
    return render(request,'AppSnake/Inicio.html')

def cientificos(request):
   
    return render(request,'AppSnake/Cientificos.html')

def medicos(request):
    medicos= Medicos.objects.all()
    contexto= {"medicos":medicos}
    return render(request,'AppSnake/medicos.html',contexto) 

def proyecto(request):

    return render(request,'AppSnake/Proyecto.html')

def medicoFormulario(request):
    if request.method == "POST":
        miFormulario=form_medicos(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            medico= Medicos(nombre=informacion['nombre'],credencial=informacion['credencial'],apellido= informacion['apellido'],interno= informacion['interno'])
            medico.save()
            return render(request,'AppSnake/inicio.html') 
    else:
        miFormulario=form_medicos()
    return render(request,'AppSnake/medicoFormulario.html',{'miFormulario':miFormulario})

def medicoBusqueda(request):
    return render(request,'AppSnake/medicoBusqueda.html',{"medicos":medicos})

def buscar(request):
    if request.GET["credencial"]:

        credencial=request.GET["credencial"]
        medicos=Medicos.objects.filter(credencial__icontains=credencial)

        return render(request,"AppSnake/resultadoBusqueda.html",{"medicos":medicos,"credencial":credencial})
    else:
        respuesta='No enviaste datos'
       
    return HttpResponse(respuesta)