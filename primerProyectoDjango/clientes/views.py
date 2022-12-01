from django.shortcuts import render

from clientes.models import Cliente


# Create your views here.
def insertar(request):
    mensaje = ""

    #Recojo los datos del formulario
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            apellidos = request.POST['apellidos']
            dni = request.POST['dni']
            email = request.POST['email']

            #Creo el objeto cliente y lo guardo
            cliente = Cliente(nombre = nombre, apellidos = apellidos, dni = dni, email = email)
            cliente.save()
        except Exception as e:
            mensaje = "Error al almacenar el cliente"
        else:
            mensaje = "Cliente insertado"

    contexto = {"mensaje": mensaje}

    return render(request, "insertar.html", contexto)
