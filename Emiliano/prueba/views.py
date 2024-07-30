from django.shortcuts import render
from django.http import HttpResponse
from prueba.forms import CursoFormulario
from prueba.models import Curso,Estudiante
from prueba.forms1 import EstudianteFormulario

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



def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "prueba/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "prueba/form_con_api.html", {"mi_formulario": mi_formulario})

def form_est(request):
    if request.method == "POST":
        mi_form = EstudianteFormulario(request.POST) 
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            estudiante.save()

            return render(request, "prueba/index.html")
    else:
        mi_form = EstudianteFormulario()

    return render(request, "prueba/form_est.html", {"mi_form": mi_form})