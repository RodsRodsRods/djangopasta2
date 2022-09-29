from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html',context = {
        'name': 'Rodox',
    })

def contato(request):
    return render(request,'temp.html')

def sobre(request):
    return HttpResponse('SOBRE')


# Create your views here.
