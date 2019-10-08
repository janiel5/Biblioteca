from django.db import models
from django.conf import settings


class Autor(models.Model):
    class Autor:
        verbose_nome_plural = "autores"

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)

    def __str__(self):
        return  self.sobrenome.upper() + ',' + self.nome

class Aluno(models.Model):
    matricula = models.CharField(max_length=12, unique=True)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ano_publicado = models.IntegerField()

    def __str__(self):
        return "{}, ({})".format(self.titulo, self.ano_publicado)

class Emprestismo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    livros = models.ManyToManyField(Livro)
    devolvido = models.BooleanField()
# Create your models here.
