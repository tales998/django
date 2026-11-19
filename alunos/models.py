from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)


def __str__(self):
    return self.nome
