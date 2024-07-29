from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render (request, "prueba/index.html")

def cursos(request):
    return render (request, "prueba/cursos.html")

def profesores(request):
    return render (request, "prueba/profesores.html")

def estudiantes(request):
    return render (request, "prueba/estudiantes.html")

def entregables(request):
    return render (request, "prueba/entregables.html")