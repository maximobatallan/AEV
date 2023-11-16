from django.db import models

# Create your models here.

class formulario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=55)
    telefono = models.CharField(max_length=55)
    categoria = models.CharField(max_length=55)
    mail = models.EmailField(max_length=55)
    texto = models.CharField(max_length=255)