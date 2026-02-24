from django.shortcuts import render, redirect
from .forms import CarroForm
from .models import Carro
# Create your views here.

def novo_carro(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            form = CarroForm()
            return render(request, 'carros/novo_carro.html', {'formulario_carro': form})
        else:
            form = CarroForm(request.POST)
            if form.is_valid():
                nome_do_carro = form.data['nome_do_carro']
                preco = form.data['preco']
                ano = form.data['ano']
                novo_carro = Carro.objects.create(nome_do_carro= nome_do_carro,
                                    preco = preco,
                                    ano = ano)
                novo_carro.save()
                return redirect('home')
    return redirect('login_user')