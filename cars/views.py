from django.shortcuts import render
from .forms import CarrosForm
from .models import Carros
from django.http import HttpResponse
# Create your views here.

def novo_carro_form(request):
    if request.method == 'GET':
        return render(request, 'carros/novo_carro.html', {'novo_carro_form': CarrosForm})
    else:
        nome_do_carro = request.POST.get('nome_do_carro')
        preco = request.POST.get('preco')
        ano = request.POST.get('ano')
        foto_carro = request.POST.get('foto_carro')
        novo_carro = Carros.objects.create(nome_do_carro= nome_do_carro,
                                           preco = preco,
                                           ano = ano,
                                           foto_carro = foto_carro)
        novo_carro.save()
        return HttpResponse({'mensagem': 'Carro salvo no banco'})
