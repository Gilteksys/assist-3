from django.db import models

class Cliente(models.Model):

    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=50)
    contato = models.CharField(max_length=20)
    documento = models.CharField(max_length=20)

class OrdemServico(models.Model):
    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    aparelho = models.CharField(max_length=200)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=20)
    serial = models.CharField(max_length=20)
    observacao = models.TextField()




   
