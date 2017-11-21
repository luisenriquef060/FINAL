from django.contrib import admin
from examen.models import Grados
from examen.models import Alumno
from examen.models import Materia

class GradosModelAdmin(admin.ModelAdmin):
    list_display= ["Nombre_Grado","Materias"]
    list_display_links = ["Materias"]
    list_filter = ["Materias"]
    list_editable = ["Nombre_Grado"]
    search_fields = ["Materias"]
    class Meta:
        model = Grados

class AlumnoModelAdmin(admin.ModelAdmin):
    list_display= ["user","Nombre_Completo","Direccion","Anio_nacimiento","Grado","created_date"]
    list_display_links = ["user"]
    list_filter = ["user"]
    list_editable = ["Nombre_Completo"]
    search_fields = ["user"]
    class Meta:
        model = Alumno

class MateriaModelAdmin(admin.ModelAdmin):
    list_display= ["Nombre_materia","Descripcion"]
    list_display_links = ["Descripcion"]
    list_filter = ["Descripcion"]
    list_editable = ["Nombre_materia"]
    search_fields = ["Descripcion"]
    class Meta:
        model = Materia

admin.site.register(Grados, GradosModelAdmin)
admin.site.register(Alumno,AlumnoModelAdmin)
admin.site.register(Materia,MateriaModelAdmin)
