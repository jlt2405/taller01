from django.db import models

class Cliente(models.Model):
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    correoelectronico = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.apellidos} {self.nombres}"
