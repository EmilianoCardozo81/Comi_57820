from django.shortcuts import render
from django.http import HttpResponse
from prueba.models import *
from prueba.forms import *


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

def form_curso(request):
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

    return render(request, "prueba/form_curso.html", {"mi_formulario": mi_formulario})

def form_estudiante(request):
    if request.method == "POST":
        mi_form = EstudianteFormulario(request.POST) 
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            estudiante.save()

            return render(request, "prueba/index.html")
    else:
        mi_form = EstudianteFormulario()

    return render(request, "prueba/form_estudiante.html", {"mi_form": mi_form})



def buscar_curso(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "prueba/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "prueba/buscar_curso.html", {"mi_formulario": mi_formulario})
    
def form_profesor(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            profesor.save()

            return render(request, "prueba/index.html")
    else:
        mi_formulario = ProfesorFormulario()

    return render(request, "prueba/form_profesor.html", {"mi_formulario": mi_formulario})