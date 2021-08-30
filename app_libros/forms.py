from django import forms
from .models import Autor, Libro, Reserva
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, PermissionsMixin



class ReservaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['libro'].queryset = Libro.objects.filter(estado = True, cantidad__gte = 1)

    class Meta:
        model = Reserva
        fields = '__all__'



'''
Registro de Usuario con funciónes  http://127.0.0.1:8000/registro/
📦registration
 ┣ 📜403.html
 ┣ 📜login.html
 ┣ 📜logout.html
 ┗ 📜registro.html **
'''
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User 
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

'''
Registro de Usuario con clases 

''' 


class RegistroForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
    label = {'username' : 'Nombre de Usuario',
            "first_name" : 'Nombre',
            "last_name" : 'Apellido',
            "email" : 'Correo',
            "password1" : 'Password1',
            "password2" : 'Password2',

    }

    def cleaned_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2 :
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class Autor_Form(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']


class Libro_Form(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor_id', 'fecha_publicacion']
        label = {
            'titulo': 'Titulo del Libro',
            'autor_id': 'Autor(res) del ibro',
            'fecha_publicacion': 'Fecha de Publicacion del Libro'
            }
        widget ={
                'titulo':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Titulo del Libro'
                }
            ),
            'autor':forms.SelectMultiple(
            attrs = {
                'class':'form-control'
            }
        ),
        'fecha_publicacion': forms.DateTimeInput(
            attrs = {
                'class' : 'form-control'
            }
        ),
        }

