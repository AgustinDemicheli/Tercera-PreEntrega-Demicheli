from django.shortcuts import render
from django.http import HttpResponse
from AppSnake.models import *

#from django.http import HttpResponse
from AppSnake.forms import form_medicos,form_cientificos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def inicio(request):
    
    return render(request,'AppSnake/Inicio.html')


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

def cientificos(request):
    cientificos= Cientificos.objects.all()
    contexto= {"cientificos":cientificos}
    return render(request,'AppSnake/cientificos.html',contexto)
 
def cientificoFormulario(request):
    if request.method == "POST":
        miFormulario=form_cientificos(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            cientifico= Cientificos(nombre=informacion['nombre'],comision=informacion['comision'],apellido= informacion['apellido'])
            cientifico.save()
            return render(request,'AppSnake/inicio.html') 
    else:
        miFormulario=form_cientificos()
    return render(request,'AppSnake/cientificoFormulario.html',{'miFormulario':miFormulario})

def cientificoBusqueda(request):
    return render(request,'AppSnake/cientificoBusqueda.html',{"cientifico":cientificos})

def buscar2(request):
    if request.GET["apellido"]:

        apellido=request.GET["apellido"]
        cientificos=Cientificos.objects.filter(apellido__icontains=apellido)

        return render(request,"AppSnake/resultadoBusqueda2.html",{"cientificos":cientificos,"apellido":apellido})
    else:
        respuesta='No enviaste datos'
       
    return HttpResponse(respuesta)