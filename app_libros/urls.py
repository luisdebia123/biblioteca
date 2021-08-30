from django.urls import path
from .import views
from .views import *
from . formsets import FormsetAutor

from django.contrib.auth.decorators import login_required, permission_required

app_name='app_libros'

urlpatterns = [    
    # path('', views.home, name='home'),
    # path('crear_autor/', views.crear_autor, name='crear_autor'),
    # path('leer_autores/', views.leer_autores, name='leer_autores'),
    # path('editar_autor/<int:id>', views.editar_autor, name='editar_autor'),
    path('eliminar_autor/<int:id>', views.eliminar_autor, name='eliminar_autor'),
    path('eliminar_SweetAlert/<id>/', views.eliminar_SweetAlert, name='eliminar_SweetAlert'),
    # path('eliminacion_logica/<int:id>/', views.eliminacion_logica, name='eliminacion_logica'),
    path('registro/',views.registro, name='registro'),

    # Con clases, Autores

    path('',Inicio.as_view(), name='home'),
    path('crear_autor/',Crear_Autor.as_view(), name='crear_autor'),
    path('leer_autores/',Leer_Autores.as_view(), name='leer_autores'),
    path('editar_autor/<int:pk>',Editar_Autor.as_view(), name='editar_autor'),
    path('eliminacion_logica/<int:pk>',EliminacionAutor.as_view(), name='eliminacion_logica'),

    # Con clases, Libros

    path('crear_libros/',Crear_Libro.as_view(), name='crear_libros'),
    path('listar_libros/', Listado_Libros.as_view(), name='listar_libros'),
    path('editar_libro/<int:pk>',Actualizar_Libro.as_view(), name='editar_libro'),
    path('eliminar_libros/<int:pk>',Eliminar_Libros.as_view(), name='eliminar_libros'),

    # Listar y crear libros en el mismo template
    path('listar_registrar_libros/', Listado_Registro_Libros.as_view(), name='listar_registrar_libros'),

    # Vistas Modal
    path('modal_listar_libros/', Modal_Listado_Libros.as_view(), name='modal_listar_libros'),
    path('modal_editar_libro/<int:pk>',Modal_Actualizar_Libro.as_view(), name='modal_editar_libro'),
    path('modal_crear_libros/',Modal_Crear_Libros.as_view(), name='modal_crear_libros'),

    path('registro_clase/',RegistroUsuario.as_view(), name='registro_clase'),
    path('libros_disponibles/',List_Libros_Disponibles.as_view(), name='libros_disponibles'),
    path('detalle_libro_disponible/<int:pk>',Detalle_Libro_Disponible.as_view(), name='detalle_libro_disponible'),
    path('reservar_libro/',RegistrarReserva.as_view(), name='reservar_libro'),
    path('libros_reservados/',Listado_Libros_Reservados.as_view(), name='libros_reservados'),

    # FORMSETS
    path('autor_formset', FormsetAutor.as_view(), name='autor_formset'),
]
