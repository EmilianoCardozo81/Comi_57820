from django.urls import path
from prueba import views

urlpatterns = [
    path('', views.inicio, name ="Inicio"),
    path('cursos/', views.cursos, name ="Cursos"),
    path('profesores/', views.profesores, name ="Profesores"),
    path('estudiantes/', views.estudiantes, name ="Estudiantes"),
    path('entregables/', views.entregables, name ="Entregables"),
    path('form_curso/', views.form_curso, name="Form_Curso"),
    path('form_estudiante/', views.form_estudiante, name="Form_Estudiante"),
    path('form_profesor/', views.form_profesor, name="Form_Profesor"),
    path('buscar_curso/', views.buscar_curso, name="Buscar_Curso"),
]




