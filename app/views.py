from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Funcionario
from .forms import FuncionarioForm


class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

    def form_valid(self, form):
        messages.success(self.request, f"✅ Funcionário '{form.instance.nome}' cadastrado com sucesso!")
        return super().form_valid(form)


class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

    def form_valid(self, form):
        messages.success(self.request, f"✅ Funcionário '{form.instance.nome}' atualizado com sucesso!")
        return super().form_valid(form)


class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "lista_funcionario.html"
    context_object_name = "fun"


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "remover_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

    def form_valid(self, form):
        messages.success(self.request, f"🗑️ Funcionário '{self.object.nome}' removido com sucesso!")
        return super().form_valid(form)

