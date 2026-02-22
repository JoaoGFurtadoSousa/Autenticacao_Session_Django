from django import forms

class CarrosForm(forms.Form):
    nome_do_carro = forms.CharField(max_length=30)
    preco = forms.FloatField()
    ano = forms.IntegerField()
    foto_carro = forms.ImageField()