from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    equipo = models.CharField(max_length=40)
    edad = models.CharField(max_length=2)
    nacionalidad = models.CharField(max_length=20)
    posicion = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.equipo} {self.edad} {self.nacionalidad} {self.posicion}"
