from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosTurma


def home(request):
    return render(request,'todos/home.html')


def listar_dados_turma_por_subtipo(request, subtipo):
    dados = DadosTurma.objects.filter(codigosubtipoatividade=subtipo)
    return render(request, 'listar_dados_turma.html', {'dados': dados})
