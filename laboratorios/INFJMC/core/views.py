from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"core/home.html")
# Create your views here.

def carrera(request):
    return render(request,"core/carreras.html")

def profesores(request):
    return render(request,"core/docentes.html")