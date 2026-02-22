from django.contrib import admin
from .models import Carros
# Register your models here.

@admin.register(Carros)
class CarrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_do_carro', 'preco', 'ano', 'foto_carro', )
    list_editable = ('preco', )
    list_filter = ('ano', )
    search_fields = ('nome_do_carro',)