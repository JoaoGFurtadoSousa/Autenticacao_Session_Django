from django.urls import path, include
from .views import novo_carro_form

urlpatterns = [
    path('novo_carro', novo_carro_form, name = 'novo_carro'),
]