from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models.functions import Concat
from django.db.models import Value
from django.contrib.admin.views.decorators import staff_member_required
from exames.models import SolicitacaoExame
from django.http import HttpResponse, FileResponse
<<<<<<< HEAD
from .utils import gerar_pdf_exames, gerar_senha_aleatoria
from django.contrib import messages
from django.contrib.messages import constants
=======
<<<<<<< HEAD
=======
from .utils import gerar_pdf_exames, gerar_senha_aleatoria
from django.contrib import messages
from django.contrib.messages import constants
>>>>>>> 033e1f463262c97baaabaa19bcedec2b351db03a
>>>>>>> 5b8980534c16ca9ac7ad3849a30921995ea34356

@staff_member_required
def gerenciar_clientes(request):
    clientes = User.objects.filter(is_staff=False)

    nome_completo = request.GET.get('nome')
    email = request.GET.get('email')

    if email:
        clientes = clientes.filter(email__contains = email)
    if nome_completo:
        clientes = clientes.annotate(full_name=Concat('first_name', Value(' '), 'last_name')).filter(full_name__contains=nome_completo)
    
    return render(request, 'gerenciar_clientes.html', {'clientes':clientes})

@staff_member_required 
def cliente(request, cliente_id):
    cliente = User.objects.get(id=cliente_id)
    exames = SolicitacaoExame.objects.filter(usuario=cliente)
    return render(request, 'cliente.html', {'cliente': cliente, 'exames': exames})

@staff_member_required
def exame_cliente(request, exame_id):
    exame = SolicitacaoExame.objects.get(id=exame_id)
    return render(request, 'exame_cliente.html', {'exame': exame})

def proxy_pdf(request, exame_id):
    exame = SolicitacaoExame.objects.get(id=exame_id)

    response = exame.resultado.open()

<<<<<<< HEAD
=======
<<<<<<< HEAD
    return HttpResponse(response)
=======
>>>>>>> 5b8980534c16ca9ac7ad3849a30921995ea34356
    return HttpResponse(response)

def gerar_senha(request, exame_id):
    exame = SolicitacaoExame.objects.get(id=exame_id)

    if exame.senha:
        return FileResponse(gerar_pdf_exames(exame.exame.nome, exame.usuario.first_name, exame.senha), filename="token.pdf")
    
    exame.senha = gerar_senha_aleatoria(9)
    exame.save()
    return FileResponse(gerar_pdf_exames(exame.exame.nome, exame.usuario.first_name, exame.senha), filename="token.pdf")

def alterar_dados_exame(request, exame_id):
    exame = SolicitacaoExame.objects.get(id=exame_id)

    pdf = request.FILES.get('resultado')
    status = request.POST.get('status')
    requer_senha = request.POST.get('requer_senha')

    if requer_senha and (not exame.senha):
        messages.add_message(request, constants.ERROR, 'Para exigir a senha primeiro crie uma.')
        return redirect(f'/empresarial/exame_cliente/{exame_id}')
    
    exame.requer_senha = True if requer_senha else False

    if pdf:
        exame.resultado = pdf
        
    exame.status = status
    exame.save()
    messages.add_message(request, constants.SUCCESS, 'Alteração realizada com sucesso')
    return redirect(f'/empresarial/exame_cliente/{exame_id}')
<<<<<<< HEAD
=======
>>>>>>> 033e1f463262c97baaabaa19bcedec2b351db03a
>>>>>>> 5b8980534c16ca9ac7ad3849a30921995ea34356
