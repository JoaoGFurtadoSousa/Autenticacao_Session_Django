from django.shortcuts import render, redirect
from .forms import CarrosForm
from .models import Carros
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def novo_carro_form(request):
    if request.session.get('user_session'):
        if request.method == 'GET':
            return render(request, 'carros/novo_carro.html', {'novo_carro_form': CarrosForm})
        else:
            form_carro = CarrosForm(request.POST)
            print(request.POST)
            if form_carro.is_valid():
                nome_do_carro = form_carro.data['nome_do_carro']
                preco = form_carro.data['preco']
                ano = form_carro.data['ano']
                foto_carro = form_carro.data['foto_carro']
                novo_carro = Carros.objects.create(nome_do_carro= nome_do_carro,
                                                preco = preco,
                                                ano = ano,
                                                foto_carro = foto_carro)
                novo_carro.save()
                return HttpResponse({'mensagem': 'Carro salvo no banco'})
            else:
                return render(request, 'carros/novo_carro.html', {'novo_carro_form': form_carro})
    return redirect('login_user')