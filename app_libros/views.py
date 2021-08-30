
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

import random
import csv
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin
from functools import wraps
from urllib.parse import urlparse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.shortcuts import reverse, redirect
from django.utils.http import urlencode
from django import forms
from django.core.paginator import Paginator
from .forms import  CustomUserCreationForm
import sweetify

from django.core.exceptions import ObjectDoesNotExist
from .forms import Autor_Form, Libro_Form, RegistroForm
from .models import Autor, Libro, Reserva

# vistas basadas en classes
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, View, DetailView
from django.urls import reverse_lazy
from .mixin import Super_Usuario_Mixin



# Create your views here.

''' con función
def home(request):
    return render(request,'app_libros/home.html')
'''
class Inicio(TemplateView):
    template_name ='app_libros/home.html'


''' con función
def crear_autor(request):
    if request.method =='GET':
        form = Autor_Form()
        context = {'form': form}
        return render(request,'app_libros/crear_autor.html', context)
    if request.method == 'POST':
        form = Autor_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_libros:home')
'''

class Crear_Autor(CreateView):
    model = Autor
    form_class = Autor_Form
    template_name = 'app_libros/crear_autor.html'
    success_url = reverse_lazy('app_libros:leer_autores')




''' con función 
def leer_autores(request):
    #autores= Autor.objects.all()
    autores= Autor.objects.filter(estado=True) # para listar registros estado True
    print(autores)
    context ={'autores' : autores}
    return render(request,'app_libros/leer_autores.html', context)
'''  

class Leer_Autores(LoginRequiredMixin, Super_Usuario_Mixin, ListView):
    model = Autor
    paginate_by = 8 
    template_name = 'app_libros/leer_autores.html'
    queryset = Autor.objects.filter(estado=True)
'''
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
'''
# En leer_autores.html se debe cambiar {% for autor in autores %}
# por {% for autor in object_list %} lo retorna como una lista de objetos
    
''' con función
def editar_autor(request,id):
    autor = Autor.objects.get(id=id)
    if request.method == 'GET':
        autor_form = Autor_Form(instance=autor)
        context ={'autor_form' : autor_form, 'id': id}
        return render(request,'app_libros/editar_autor.html', context)
    else:
        autor_form = Autor_Form(request.POST, instance=autor)
        if autor_form.is_valid():
            autor_form.save()
            messages.success(request, 'Modificado correctamente')
            return redirect('app_libros:leer_autores')
    return render(request,'app_libros/editar_autor.html', context)
'''

class Editar_Autor(SuccessMessageMixin, UpdateView):
    model = Autor
    template_name = 'app_libros/editar_autor.html'
    form_class = Autor_Form
    success_url = reverse_lazy('app_libros:leer_autores')
    success_message = 'Modificado correctamente'


def eliminar_autor(request, id):
    autor = Autor.objects.get(id=id)
    if request.method == "GET":
        autor = Autor_Form(instance=autor)
        context = {'id': id, 'autor' : autor}
        return render(request, "app_libros/eliminar_autor.html", context)
    if request.method == "POST":
        Autor.objects.filter(id=id).delete()
        messages.success(request, 'Eliminado correctamente')
        return redirect('app_libros:leer_autores')

def eliminar_SweetAlert(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    messages.success(request, 'Eliminado correctamente')
    return redirect('app_libros:leer_autores')



''' con función
def eliminacion_logica(request, id):
    autor = Autor.objects.get(id=id)
    if request.method == "GET":
        autor = Autor_Form(instance=autor)
        context = {'id': id, 'autor' : autor}
        return render(request, "app_libros/eliminacion_logica.html", context)
    if request.method == "POST":
        autor.estado = False
        autor.save()
        messages.success(request, 'Eliminado correctamente')
        return redirect('app_libros:leer_autores')
'''

# Eliminación directa utiliza template autor_confirm_delete.html
'''
class EliminacionAutor(DeleteView):
    model = Autor
    success_url =reverse_lazy('app_libros:leer_autores') 
'''

# Eliminación lógica
class EliminacionAutor(SuccessMessageMixin, DeleteView):
    model = Autor
    
            
    def post(self, request,pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        messages.success(request, 'Eliminado correctamente')
        return redirect('app_libros:leer_autores')


def registro(request):
    data= {'form': CustomUserCreationForm()}

    if request.method =="POST":
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],
            password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado OK.")
            return redirect('/')
        data["form"] = formulario      
    return render(request, 'registration/registro.html', data)

class Listado_Libros(ListView):
    model = Libro
    template_name = "app_libros/listar_libros.html" #queryset = libro.objects.all() object_list()
    queryset = Libro.objects.filter(estado=True)

    

class Crear_Libro(CreateView):
    model = Libro
    form_class = Libro_Form
    template_name ='app_libros/crear_libros.html'
    success_url = reverse_lazy('app_libros:listar_libros')


class Actualizar_Libro(SuccessMessageMixin, UpdateView):
    model = Libro
    template_name = 'app_libros/editar_libro.html'
    form_class = Libro_Form
    success_url = reverse_lazy('app_libros:listar_libros')
    success_message = 'Modificado correctamente'

class Eliminar_Libros(SuccessMessageMixin, DeleteView):
    model = Libro

    def post(self, request,pk, *args, **kwargs):
        object = Libro.objects.get(id=pk)
        object.estado = False
        object.save()
        messages.success(request, 'Eliminado correctamente')
        return redirect('app_libros:listar_libros')


# Crear listado y Registro de Libros en un solo template.
class Listado_Registro_Libros(View):
    model = Libro
    form_class = Libro_Form
    template_name = "app_libros/listar_registrar_libros.html" 
    
    def get_queryset(self,): # Returna la consulta.
        return self.model.objects.filter (estado=True)
    
    def get_context_data(self, **kwargs): # Retorna el contenido de la información enviada al template
        context ={}
        context ['libros'] = self.get_queryset()
        context ['form'] = self.form_class
        return context

    def get(self,request, *args, **kwargs): # retorna toda la información
        return render(request,self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_libros:listar_registrar_libros')
        else:
            form = self.form_class()
            return render(request,self.template_name,self.get_context_data())

    
# Crear vistas tipo modal

class Modal_Actualizar_Libro(SuccessMessageMixin, UpdateView):
    model = Libro
    form_class = Libro_Form
    template_name = 'app_libros/modal_libro.html'
    success_url = reverse_lazy('app_libros:modal_listar_libros')
    success_message = 'Modificado correctamente'


'''
    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libro'] = Libro.objects.filter(estado=True)
        return context
'''
'''
class Modal_Listado_Libros(ListView):
    model = Libro
    template_name = "app_libros/modal_listar_libros.html" #queryset = libro.objects.all() object_list()
    queryset = Libro.objects.filter(estado=True)
'''


class Modal_Listado_Libros(View):
    model = Libro
    form_class = Libro_Form
    template_name = "app_libros/Modal_listar_libros.html" 
    
    def get_queryset(self): # Returna la consulta.
        return self.model.objects.filter (estado=True)


    
    def get_context_data(self, **kwargs): # Retorna el contenido de la información enviada al template
        context ={}
        context ['libros'] = self.get_queryset()
        context ['form'] = self.form_class
        return context

    def get(self,request, *args, **kwargs): # retorna toda la información
        return render(request,self.template_name, self.get_context_data())

class Modal_Crear_Libros(CreateView):
    model = Libro
    form_class = Libro_Form
    template_name = 'app_libros/modal_crear_libros.html'
    success_url = reverse_lazy('app_libros:modal_listar_libros')


# Registro de usuario con clases
class RegistroUsuario(CreateView):
    model = User
    count = User.objects.count()
    template_name = 'app_libros/registro_clase.html'
    form_class = RegistroForm
    success_url = reverse_lazy('app_libros:home')

class List_Libros_Disponibles(ListView):
    model = Libro
    paginate_by = 4
    template_name = 'app_libros/libros_disponibles.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(estado=True ,cantidad__gte = 0)
        return queryset

class Detalle_Libro_Disponible(DetailView):
    model = Libro
    template_name = 'app_libros/detalle_libro_disponible.html'

class RegistrarReserva(CreateView):
    model = Reserva
    success_url = reverse_lazy('app_libros:libros_disponibles')
    success_message = 'Modificado correctamente'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            libro = Libro.objects.filter(id = request.POST.get('libro')).first()
            usuario = request.user
            if libro and usuario :
                nueva_reserva = self.model(
                    libro = libro,
                    usuario = usuario
                )
                nueva_reserva.save()

                mensaje = f'{self.model.__name__} Registrada Correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje':mensaje, 'error' :error, 'url':self.success_url})
                print(response)
                response.status_code = 201
                
                return redirect('app_libros:libros_disponibles')
                print(request.POST)

        return redirect('app_libros:libros_disponibles')

class Listado_Libros_Reservados(ListView):
    model = Reserva
    paginate_by = 6
    template_name = 'app_libros/libros_reservados.html'
    queryset = Reserva.objects.filter(estado=True)




















