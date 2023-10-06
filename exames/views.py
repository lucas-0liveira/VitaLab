from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from .models import TiposExames
from datetime import date
import locale

@login_required
def solicitar_exames(request):
    tipos_exames = TiposExames.objects.all()

    #Obtém a data atual
    data_atual = date.today()
    # Configura o locale para sua localidade
    locale.setlocale(locale.LC_ALL, '')
    #Converte a data para o formato desejado
    data_formatada = data_atual.strftime('%d de %B de %Y')

    if request.method == "GET":
        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames, 'data_atual': data_formatada})
    elif request.method == "POST":
        exames_id = request.POST.getlist('exames')
        solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
        
        #TODO: Calcular o preço dos dados disponíveis
        preco_total = 0
        for i in solicitacao_exames:
            if i.disponivel:
                preco_total += i.preco


        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames,
                                                         'solicitacao_exames': solicitacao_exames,
                                                         'preco_total': preco_total, 'data_atual': data_formatada})
    
def fechar_pedido(request):
    exames_id = request.POST.getlist('exames')

    return HttpResponse('Estou aqui')
    
