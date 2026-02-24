from django import forms

class CarroForm(forms.Form):
    nome_do_carro = forms.CharField(max_length= 50)
    preco = forms.FloatField()
    ano = forms.IntegerField()