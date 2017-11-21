from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Materia(models.Model):
    Nombre_materia = models.CharField(max_length=200)
    Descripcion =models.CharField(max_length=200)

    def __unicode__(self):
        return self.Nombre_materia

    def __str__(self):
        return self.Nombre_materia

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

class Grados(models.Model):
    Nombre_Grado = models.CharField(max_length=200)
    Materias = models.ForeignKey(Materia,related_name ='Materia')


    def __unicode__(self):
        return self.Nombre_Grado

    def __str__(self):
        return self.Nombre_Grado

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

class Alumno(models.Model):
    user = models.ForeignKey('auth.User')
    Nombre_Completo = models.CharField(max_length=200)
    Direccion =models.CharField(max_length=200)
    Anio_nacimiento = models.DateTimeField(auto_now=False, auto_now_add=False)
    Grado = models.ForeignKey(Grados,related_name ='grados')
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.Nombre_Completo

    def __str__(self):
        return self.Nombre_Completo

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
