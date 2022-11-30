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
    continente_filtro = None
    if request.method == 'POST':
        continente_filtro = request.POST['continente']
        titulo = request.POST['titulo']
    elif request.method == 'GET':
        # titulo = request.parameter("titulo")
        titulo = request.GET['titulo']

    espania = {"nombre": "España", "continente": "Europa", "num_mundiales": 1}
    brasil = {"nombre": "Brasil", "continente": "America", "num_mundiales": 5}
    francia = {"nombre": "Francia", "continente": "Europa", "num_mundiales": 2}
    senegal = {"nombre": "Senegal", "continente": "Africa", "num_mundiales": 0}

    lista_selecciones = [espania, brasil, francia, senegal]
    if not continente_filtro == None:
        lista_selecciones = list(
            filter(lambda seleccion: seleccion["continente"] == continente_filtro, lista_selecciones))

    contexto = {"listado_selecciones": lista_selecciones, "titulo_tabla": titulo,
                "listado_continentes": ["Europa", "America", "Asia", "Africa", "Oceania"]}

    return render(request, "listado_selecciones_mundial.html", contexto)