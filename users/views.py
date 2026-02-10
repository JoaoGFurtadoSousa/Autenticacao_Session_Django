from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from hashlib import sha256


def criptografa_password(password: str):
    bytes_password = password.encode("utf-8")
    sha = sha256()
    sha.update(bytes_password)
    password_hash = sha.hexdigest()
    return password_hash

def valida_tamanho_username(username: str):
    if len(username.strip()) <= 2:
        return False
    return username

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = valida_tamanho_username(username= username)
        print(username)
        if Users.objects.filter(email = email).exists():
            return HttpResponse('Usuario com email já cadastrado')
    
        if username:
            print(username)
            password = criptografa_password(password= password)
            usuario = Users.objects.create(username= username, email= email, password= password)
            return HttpResponse({'response': '201'})
        return HttpResponse('Nome menor que três caracteres')
    return render(request, 'cadastro/cadastro.html')
