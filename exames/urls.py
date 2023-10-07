from django.urls import path
from . import views

urlpatterns = [
    path('solicitar_exames/', views.solicitar_exames, name="solicitar_exames"),
    path('fechar_pedido/', views.fechar_pedido, name="fechar_pedido"),
    path('gerenciar_pedidos/', views.gerenciar_pedidos, name="gerenciar_pedidos"),
    path('cancelar_pedido/<int:pedido_id>', views.cancelar_pedido, name="cancelar_pedido"),
    path('gerenciar_exames/', views.gerenciar_exames, name="gerenciar_exames"),
]

