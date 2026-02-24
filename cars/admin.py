from django.contrib import admin
from .models import Carro
# Register your models here.

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_do_carro', 'preco', 'ano', )
    search_fields = ('nome_do_carro',)
    list_editable = ('preco', )
    