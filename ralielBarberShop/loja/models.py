from django.conf import settings
from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length = 50)
    CATEGORIA = (
        ('H', 'Homem'),
        ('M', 'Mulher'),
        ('C', 'Criança'),
        ('U', 'Unisex'),
    )
    categoria = models.CharField(max_length = 1, choices = CATEGORIA)

class Marca(models.Model):
    nome = models.CharField(max_length = 50)
    quantidadeProdutos = models.IntegerField(default = 0)

class Produto(models.Model):
    nome = models.CharField(max_length = 50)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = True, blank = True)
    marca = models.ForeignKey(Marca, on_delete = models.CASCADE, null = True, blank = True)
    preco = models.FloatField()
    quantidade = models.IntegerField(default = 0)
    descricao = models.TextField()

