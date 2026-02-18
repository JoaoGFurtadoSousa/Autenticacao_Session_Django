from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from hashlib import sha256
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect


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
        if User.objects.filter(email = email).exists():
            return HttpResponse('Usuario com email já cadastrado')
    
        if username:
            usuario = User.objects.create_user(username= username, email= email, password= password)
            return redirect('login_user')
        return HttpResponse('Nome menor que três caracteres')
    return render(request, 'cadastro/cadastro.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            usuario = User.objects.get(email = email)
        except User.DoesNotExist:
            print('Usuario não existe')
            return redirect('login_user')
        
        print(usuario.password)
        if check_password(password= password, encoded=usuario.password):
            request.session['user_session'] = usuario.id
            return redirect('home')
        print('senha incorreta')
    return render(request, 'login/login.html')

def logout(request):
    request.session.flush()
    return redirect('login_user')

def home(request):
    if request.session.get('user_session'): #tenta encontrar dentro da session_data alguma chave de dict assim
        lista_de_pessoas = User.objects.all()
        return render(request, 'home.html', {'pessoas': lista_de_pessoas})
    return redirect('login_user')

def change_user(request):
   if request.method == "POST":
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')

       usuario = User.objects.filter(username = username)
       print(usuario)
       if usuario:
           password = make_password(password)
           usuario.username = username
           usuario.email = email
           usuario.password = password
           usuario.save()
        
       return redirect('login_user')
   return redirect('change_user')