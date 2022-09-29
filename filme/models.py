from django.db import models
from django.utils import timezone

# Create your models here.
LISTA_CATEGORIAS = (
    ("ACAO", "Ação"),
    ("AVENTURA", "Aventura"),
    ("ANIME", "Animes"),
    ("OUTROS", "Outros"),
)
# Criar filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# Criar episódios

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - "+ self.titulo
    # Para não aparecer no admin episodio.object

 # Foreignkey =Cria um item dentro do episódio, cria um item dentro de filmes, um episódio só pode
    # ter um único filme relacionado a ele
    #Primeiro parametro: Nome da tabela com que ele tem que se relacionar, entre aspas
    #Segundo parametro: related name
    #Terceiro parametro: Models.CASCADE - Caso o filme seja deletado, ele vai deletar todos os episodios relacionados
# a aquele filme


# Criar usuário