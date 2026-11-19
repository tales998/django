from django.shortcuts import render
from .models import Aluno

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        aluno = Aluno(nome=nome, idade=idade, email=email, telefone=telefone, endereco=endereco)
        aluno.save()

    return render(request, 'alunos/cadastrar.html')

def listar(request):
    alunos = Aluno.objects.all()
    return render(request, "alunos/listar.html", {"alunos": alunos})