from django.urls import path
from .views import novo_carro

urlpatterns = [
   path('novo_carro', novo_carro, name = 'novo_carro'),
]