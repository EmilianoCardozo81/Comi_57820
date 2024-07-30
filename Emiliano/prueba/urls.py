from django.urls import path
from prueba import views

urlpatterns = [
    path('', views.inicio, name ="Inicio"),
    path('cursos/', views.cursos, name ="Cursos"),
    path('profesores/', views.profesores, name ="Profesores"),
    path('estudiantes/', views.estudiantes, name ="Estudiantes"),
    path('entregables/', views.entregables, name ="Entregables"),
    path('form-con-api/', views.form_con_api, name="FormConApi"),
    path('form_est/', views.form_est, name="Form_Est"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]




