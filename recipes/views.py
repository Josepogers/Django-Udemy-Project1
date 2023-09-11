from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/home.html', context={ 'name': 'José Francisco',})

def contato(request):
    return HttpResponse('Contato')

def sobre(request):
    return HttpResponse('sobre')