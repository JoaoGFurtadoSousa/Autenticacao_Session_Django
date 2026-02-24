from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from hashlib import sha256
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ResetPasswordForm

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
        if User.objects.filter(email = email).exists():
            return HttpResponse('Usuario com email já cadastrado')
    
        if username:
            usuario = User.objects.create_user(username= username, email= email, password= password)
            return redirect('login_user')
        return HttpResponse('Nome menor que três caracteres')
    return render(request, 'cadastro/cadastro.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        usuario = authenticate(request, username= username, password= password)
        print(usuario)
        if usuario:
            print('entorou')
            login(request, usuario)
            return redirect('home')
        print('senha incorreta')
    return render(request, 'login/login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

def home(request):
    print(request.session)
    if request.user.is_authenticated: #tenta encontrar dentro da session_data alguma chave de dict assim
        lista_de_pessoas = User.objects.all()
        return render(request, 'home.html', {'pessoas': lista_de_pessoas})
    return redirect('login_user')

def change_user(request, pk:int):
   usuario = User.objects.get(id = pk)
   if request.method == "POST":
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')
       if usuario:
           password = make_password(password) 
           usuario.username = username
           usuario.email = email
           usuario.password = password
           usuario.save()
           return redirect('home')
   return render(request, f'change_user/change_user.html/', {'usuario': usuario})

def exclude_user(request, pk: int):
    if request.method == "POST":
        usuario = User.objects.get(id = pk)
        usuario.delete()
        return redirect('home')
    
def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = valida_tamanho_username(username= username)
        if User.objects.filter(email = email).exists():
            return HttpResponse('Usuario com email já cadastrado')

        if username:
            usuario = User.objects.create_user(username= username, email= email, password= password)
            return redirect('home')
        return HttpResponse('Nome menor que três caracteres')
    return render(request, 'cadastro/novo_usuario.html')



def reset_password_user(request):
    form = ResetPasswordForm()
    if request.method == 'GET':
        return render(request, 'cadastro/reset_password.html', {'form': form})   
    elif request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password_atual = form.cleaned_data['password_atual']
            nova_password = form.cleaned_data['nova_password']
            confirmacao_password = form.cleaned_data['confirmacao_password']
            usuario = User.objects.get(username = username)
            if check_password(password_atual, usuario.password):
                if nova_password == confirmacao_password:
                    usuario.password = make_password(nova_password)
                    usuario.save()
                    return redirect('home')
                return HttpResponse('Senhas não coincidem')
            return HttpResponse('Senha atual está incorreta')
        return render(request, 'cadastro/reset_password.html', {'form': form})
