from django.db import models

# Create your models here.

class Cientificos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    comision=models.IntegerField()
    mail=models.EmailField()
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido:{self.apellido} - Comision: {self.comision}'
class Medicos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    credencial=models.IntegerField()
    interno=models.IntegerField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - N°Credencial: {self.credencial} - Interno: {self.interno}'

class Proyecto(models.Model):
    nombre=models.CharField(max_length=40)
    author=models.CharField(max_length=40,default="Anonymous")
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre