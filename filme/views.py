from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"
class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    #object_list -> lista de itens do modelo

class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    #object -> 1 item do modelo

    def get(self, request, *args, **kwargs):
        filme = self.get_object()  #descobrir qual filme ele está acessando
        filme.visualizacoes += 1  #somar 1 nas visualizações daquele filme
        filme.save()  #salvar
        return super().get(request, args, kwargs) # redireciona o usuário para o link final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # Filtrar a tabela de filmes pegando os filmes de categoria igual (object)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context["filmes_relacionados"] = filmes_relacionados
        return context


#def homefilmes(request):
#   context = {}
#    lista_filmes = Filme.objects()
#    context['lista_filmes'] = lista_filmes
#    return render(request, "homefilmes.html", context)


#def homepage(requests):
#    return render(requests, "homepage.html")
