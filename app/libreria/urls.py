from django.urls import path
from . import views
from .views import InicioView, NosotrosView, ListLibrosView, CrearLibroView, EditarLibroView, EliminarLibroView

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    #path('', views.inicio, name='inicio'),
    path('', InicioView.as_view(), name='inicio'),
    #path('nosotros', views.nosotros, name='nosotros'),
    path('nosotros', NosotrosView.as_view(), name='nosotros'),
    #path('libros', views.libros, name='libros'),
    path('libros', ListLibrosView.as_view(), name='libros'),
    #path('libros/crear', views.crear, name= 'crear'),
    path('libros/crear', CrearLibroView.as_view(), name= 'crear'),
    #path('libros/editar/<int:id>', views.editar, name='editar'),
    path('libros/editar/<int:pk>', EditarLibroView.as_view(), name='editar'),
    #path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('eliminar/<int:pk>', EliminarLibroView.as_view(), name='eliminar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)