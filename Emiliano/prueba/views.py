from django.shortcuts import render
from django.http import HttpResponse
from prueba.forms import CursoFormulario
from prueba.models import Curso,Estudiante
from prueba.forms import EstudianteFormulario
from prueba.forms import BuscaCursoForm

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



def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "prueba/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "prueba/buscar_form_con_api.html", {"mi_formulario": mi_formulario})
    