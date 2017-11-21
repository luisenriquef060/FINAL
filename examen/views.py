from django.shortcuts import render

from .models import Alumno
from .models import Grados
from .models import Materia
from .forms import AlumnoForm
from .forms import GradoForm
from .forms import MateriaForm
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse

def nuevo(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)


def nuevoG(request):
    form = GradoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)

def Materia(request):
    form = MateriaForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)



def lista(request):
    queryset = Alumno.objects.all().order_by("-created_date")
    if request.user.is_authenticated():
        context = {
            "object_list": queryset,
        }
    else:
        context = {
            "title": "Inicie sesion para ver la lista de articulos"
        }
    return render(request,"index.html",context)
