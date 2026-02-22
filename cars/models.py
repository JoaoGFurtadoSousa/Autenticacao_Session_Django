from django.db import models

# Create your models here.

class Carros(models.Model):
    nome_do_carro = models.CharField(max_length=30)
    preco = models.FloatField()
    ano = models.IntegerField()
    foto_carro = models.ImageField(upload_to='media')

    def __str__(self):
        return self.nome_do_carro
