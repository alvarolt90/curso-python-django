from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
"""
def bienvenido(request):
    return HttpResponse("Hola Mundo")

def bienvenido(request):
    return render(request, "bienvenido.html")
"""
def bienvenido(request):
    mensajes = {"mensaje1":"Valor del mensaje1", "mensaje2":"Valor del mensaje2"}
    return render(request, "bienvenido.html", mensajes)

def despedida(request):
    return render(request, "despedida.html")

def listar_alumnos(request):
    listado_alumnos = [
        {"nombre":"Nombre1", "apellidos":"Apellidos1", "dni":"1111A"},
        {"nombre":"Nombre2", "apellidos":"Apellidos2", "dni":"2222B"},
        {"nombre":"Nombre3", "apellidos":"Apellidos3", "dni":"3333C"},
    ]
    contexto = {"listado_alumnos": listado_alumnos}
    return render(request, "gestion/alumnos.html", contexto)

def equipos(request):
    equipos = [
        {"Seleccion":"España", "Continente":"Europa", "Num_mundiales":"1"},
        {"Seleccion":"Brasil", "Continente":"África", "Num_mundiales":"5"},
        {"Seleccion":"Francia", "Continente":"Europa", "Num_mundiales":"2"},
    ]
    contexto = {"equipos": equipos}
    return render(request, "equipos.html", contexto)