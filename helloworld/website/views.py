from django.shortcuts import render
from helloworld.models import Funcionario
from django.views.generic import ListView, UpdateView, DeleteView

def index(request):
    return lista_funcionarios(request)

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()
    # Incluímos no contexto
    contexto = {'funcionarios': funcionarios}
    # Retornamos o template para listar os funcionários
    return render(request, "website/lista.html", contexto)

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

class FuncionarioUpdateView(UpdateView):
    template_name = 'website/atualiza.html'
    model = Funcionario
    fields = [
        'nome',
        'sobrenome',
        'cpf',
        'tempo_de_servico',
        'remuneracao'
    ]

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")
