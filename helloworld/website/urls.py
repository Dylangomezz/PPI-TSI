# Importamos a função index() definida no arquivo views.py
from . import views
from django.urls import path



app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    path('', views.index, name='index'),
    path('funcionarios/', views.FuncionarioListView.as_view(), name='lista_funciorios'),
    path('funcionario/<id>', views.FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    path('funcionario/excluir/<pk>', views.FuncionarioDeleteView.as_view(), name='deleta_funcionario')

]
