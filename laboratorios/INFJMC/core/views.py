from django.shortcuts import render,redirect
from django.http import HttpResponse
from core.models import Carrera,docente


def home(request):
    #return HttpResponse("<h1>Home<h1/>")
    return render(request,'core/home.html')


def carrera(request):
    #return HttpResponse("<h1>Carrera<h1/>")
    carreras = Carrera.objects.all()  #Selecciona todo lo de la tabla carrera
    data = {
        'carreras': carreras
    }
    return render(request,'core/carreras.html', data)


def profe(request):
    profesores= docente.objects.all()
    data={
        'profesores':profesores
    }
    #return HttpResponse("<h1>Profesores<h1/>" + "<p> SANTUTU MI PROFE <p/>" )
    return render(request,'core/profesores.html',data)

def nueva_carrera(request):
    if request.POST:
        nombre=request.POST["nombre"]
        ident=request.POST["id"]
        duracion=request.POST["duracion"]
        c=Carrera(codigo=ident,nombre_carrera=nombre,duracion_semestres=duracion)
        c.save()
        return redirect(carrera)
    return render(request,'core/nueva_carrera.html')

def nuevo_profesor(request):
    if request.POST:
        nombre=request.POST["nombre"]
        apellidos=request.POST["apellido"]
        email= request.POST["email"]
        c=docente(nombre=nombre,apellido=apellidos,email=email)
        c.save()
        return redirect(profe)
    return render(request,'core/nuevo_profesor.html')


