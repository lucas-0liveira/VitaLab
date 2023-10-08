from django.urls import path
from . import views

urlpatterns = [
    path('gerenciar_clientes/', views.gerenciar_clientes, name="gerenciar_clientes"),
    path('cliente/<int:cliente_id>', views.cliente, name="cliente"),
]