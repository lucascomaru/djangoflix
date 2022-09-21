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


# Criar usuário