from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Tiago Cardoso'})
    # return HttpResponse('Home')


def contato(request):
    return render(request, 'recipes/contato.html', context={'name': 'Receitas Cardoso'})


def sobre(request):
    return HttpResponse('Sobre')
