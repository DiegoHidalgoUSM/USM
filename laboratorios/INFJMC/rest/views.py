from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CarreraSerializer
from core.models import Carrera
# Create your views here.
class CarreraviewSet(viewsets.ModelViewSet):
    queryset= Carrera.objects.all()
    serializer_class=CarreraSerializer