from django import forms

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()