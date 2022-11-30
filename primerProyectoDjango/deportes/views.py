from django.shortcuts import render

# Create your views here.
def deportes(request):
    contenido = {"Titulopagina":"Este es el titulo", "Descripcion":"Esta es la descripcion"}
    return render(request, "deportes.html", contenido)