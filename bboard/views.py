from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb

def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'about-us.html')
def bao(request):
    return render(request, 'bao.html')
def charyn(request):
    return render(request, 'charyn.html')
def kolsay(request):
    return render(request, 'kolsay.html')
def chymbulak(request):
    return render(request, 'chymbulak.html')
def borovoe(request):
    return render(request, 'borovoe.html')
def altay(request):
    return render(request, 'altay.html')

