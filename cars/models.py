from django.db import models

# Create your models here.

class Carro(models.Model):
    nome_do_carro = models.CharField(max_length= 50)
    preco = models.FloatField()
    ano = models.IntegerField()

    def __str__(self):
        return self.nome_do_carro