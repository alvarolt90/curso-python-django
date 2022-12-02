from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404
from deportes.models import Jugador

# Create your views here.
def deportes(request):
    contenido = {"titulo_pagina": "Actualidad deportiva",
                 "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
                                "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, "
                                "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "}
    return render(request, "deportes.html", contenido)


def listar_selecciones(request):
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

def listado_jugadores(request):
    jugadores = Jugador.objects.all()
    contexto = {"lista_jugadores": jugadores}
    return render(request, "jugadores.html", contexto)


JugadorForm = modelform_factory(Jugador, exclude=[])
def nuevo_jugador(request):
    mensaje = ''
    if request.method == 'POST':
        try:
            jugador_form = JugadorForm(request.POST)
            jugador_form.save()
        except Exception as e:
            mensaje = f'Error al insertar el jugador {e}'
        else:
            mensaje = "Jugador insertado correctamente"

    jugador_form = JugadorForm()

    contexto = {"jugador_form": jugador_form, "mensaje": mensaje}
    return render(request, "nuevo_jugador.html", contexto)