from django import forms
from .models import Alumno
from .models import Grados
from .models import Materia
from django.forms import ModelForm

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['Nombre_materia','Descripcion']

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grados
        fields = ['Nombre_Grado','Materias']

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['user', 'Nombre_Completo', 'Direccion', 'Anio_nacimiento','Grado','created_date']
