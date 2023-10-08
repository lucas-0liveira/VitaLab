from django.shortcuts import render
from django.contrib.auth.models import User

def gerenciar_clientes(request):
    clientes = User.objects.filter(is_staff=False)
    
    return render(request, 'gerenciar_clientes.html', {'clientes':clientes})
