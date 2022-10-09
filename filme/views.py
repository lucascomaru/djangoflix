from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes') #nome do app name dentro do arquivo URL
        else:
            return super().get(request, *args, **kwargs) # redireciona para a homepage

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')
class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    #object_list -> lista de itens do modelo

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    #object -> 1 item do modelo

    def get(self, request, *args, **kwargs):  # request possui método get e método post
        filme = self.get_object()  #descobrir qual filme ele está acessando
        filme.visualizacoes += 1  #somar 1 nas visualizações daquele filme
        filme.save()  #salvar
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, args, kwargs) # redireciona o usuário para o link final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # Filtrar a tabela de filmes pegando os filmes de categoria igual (object)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context["filmes_relacionados"] = filmes_relacionados
        return context

class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):  #edita o object list
        termo_pesquisa = self.request.GET.get('query') #GET = tipo de requisição / get() = pegar um parametro da
        # requisição
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')

class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)  #Salva um formulário no banco de dados
    def get_success_url(self):
        return reverse('filme:login')

#def homefilmes(request):
#   context = {}
#    lista_filmes = Filme.objects()
#    context['lista_filmes'] = lista_filmes
#    return render(request, "homefilmes.html", context)


#def homepage(requests):
#    return render(requests, "homepage.html")
