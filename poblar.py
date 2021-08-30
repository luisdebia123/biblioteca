import os
import time
import django, random as rd 
from random import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')

django.setup() # importamos el modelo

from app_libros.models import Autor

vocales =[ 'a', 'e', 'i', 'o', 'u','A','E','I','O','U']
consonates=['b', 'd', 'f', 'g', 'h', 'j',
            'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r',
            's', 't', 'v', 'x', 'y',
            'z','B','C','D','F','G','H','J','K',
            'L','M','N','Ñ','P','Q','R','S','T',
            'V','W','X','Y','Z']

def generate_string(length):
    if length <= 0:
        return False

    random_string = ''

    for i in range(length):
        decision = rd.choice(('vocales', 'consonantes'))

        if random_string[-1:].lower() in vocales:
            decision = 'consonates'
        if random_string[-1:].lower() in consonates:
            decision = 'vocales'

        if decision == 'vocales':
            caracter = rd.choice('vocales')
        else:
            caracter = rd.choice('consonantes')
        random_string += caracter
    return random_string

def generador_numeros():
    return int(random()*10+1)

def generador_autor(count):
    for j in range(count):    
        random_name = generate_string(generador_numeros())
        random_last_name = generate_string(generador_numeros())
        random_country = generate_string(generador_numeros())
        random_description = generate_string(generador_numeros())

        Autor.objects.create(
                nombre = random_name,
                apellidos = random_last_name,
                nacionalidad = random_country,
                descripcion = random_description
                )

if __name__ == '__main__':
    print(generate_string(10))


    print('Inicio de creación de datos')
    print('espere, por favor......')
    start = time.strftime("%c")
    print(f'Fecha y hora de Inicio  : {start}')
    generador_autor(50) # genera 50 registros
    end = time.strftime('%c')
    print(f'Fecha y hora de Termin  : {end}')



