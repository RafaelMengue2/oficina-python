from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    carname = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    placa = models.CharField(max_length=20)
    dono = models.CharField(max_length=100)
    defeito = models.TextField()

    def __str__(self):
        return self.carname

class Peca(models.Model):
    marca = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.marca

class Servico(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    data_servico = models.DateField()
    observacoes = models.TextField()

    def __str__(self):
        return f"{self.car.carname} - {self.peca.marca}"
    
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=50)
    numero = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


