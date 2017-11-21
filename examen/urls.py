from django.conf.urls import include,url
from examen import views as post_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_views.lista, name ="lista"),
    url(r'^nuevo/', post_views.nuevo, name ="nuevo"),
    url(r'^grado/', post_views.nuevoG, name ="nuevoU"),
    url(r'^materia/', post_views.Materia, name ="grado"),
]
