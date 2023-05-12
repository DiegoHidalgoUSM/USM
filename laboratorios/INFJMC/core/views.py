from django.shortcuts import render
from django.http import HttpResponse
from .models import carrera


def index(request):
    return render(request,"core/home.html")
# Create your views here.

def Carrera(request):
    carreras = carrera.objects.all()
    return render(request,"core/carreras.html")

def profesores(request):
    return render(request,"core/docentes.html")