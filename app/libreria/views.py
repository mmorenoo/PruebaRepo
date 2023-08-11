from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Libro
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
# def inicio(request):
#     return render(request, 'paginas/inicio.html')

class InicioView(TemplateView):
    template_name = 'paginas/inicio.html'

# def nosotros(request):
#     return render(request, 'paginas/nosotros.html')

class NosotrosView(TemplateView):
    template_name = 'paginas/nosotros.html'


# LISTAR con vistas basadas en funciones
# def libros(request):
#     libros = Libro.objects.all()
#     return render(request, 'libros/index.html', {'libros': libros})


# LISTAR con vistas basadas en clases
class ListLibrosView(ListView):
    template_name = 'libros/index.html'
    model = Libro



#CREAR con vistas basadas en funciones
# def crearLibros(request):
#     formulario = LibroForm(request.POST or None, request.FILES or None)
#     if formulario.is_valid():
#         formulario.save()
#         return redirect('libros') 
#     return render(request, 'libros/crear.html', {'formulario': formulario})


#CREAR con vistas basadas en clases
class CrearLibroView(CreateView):
    template_name = 'libros/crear.html'
    model = Libro
    fields = ['id', 'titulo', 'imagen','descripcion']
    success_url = reverse_lazy('libros')
    




#EDITAR con vistas basadas en funciones
# def editar(request, id):
#     libro = Libro.objects.get(id = id)
#     formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
#     if formulario.is_valid() and request.POST:
#         formulario.save()
#         return redirect('libros') 
#     return render(request, 'libros/editar.html', {'formulario': formulario})


#EDITAR con vistas basadas en clases
class EditarLibroView(UpdateView):
    template_name = 'libros/editar.html'
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('libros')





#ELIMINAR con vistas basadas en funciones
# def eliminar(request, id):
#     libro = Libro.objects.get(id=id)
#     libro.delete()
#     return redirect('libros')


#ELIMINAR con vistas basadas en clases Eliminacion fisica en la base de datos
# class EliminarLibroView(DeleteView):
#     template_name = 'libros/eliminar-confirmacion.html'
#     model = Libro
#     success_url = reverse_lazy('libros')
    
    
    
#ELIMINAR con vistas basadas en clases Eliminacion logica  en la aplicación
class EliminarLibroView(DeleteView):
    template_name = 'libros/eliminar-confirmacion.html'
    model = Libro
    
    def post(self, request, pk, *args, **kwargs):
        libro = Libro.objects.get(id=pk)
        libro.estado = False
        libro.save()
        return redirect('libros')
    