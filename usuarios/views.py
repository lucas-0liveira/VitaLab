from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

def cadastro (request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            return redirect('/usuarios/cadastro')
        
        try:
        #TODO: Validar se o username do usuário não existe
            user = User.objects.create_user(
                first_name = primeiro_nome,
                last_name = ultimo_nome,
                user = username,
                email = email,
                password = senha
            )
        except:
            return redirect ('/usuarios/cadastro')
        
        return redirect('/usuarios/cadastro')