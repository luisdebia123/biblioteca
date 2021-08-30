import datetime
from datetime import timedelta
from .models import Reserva
from django.contrib.auth.models import User

class PruebaMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.user.is_authenticated:
            fecha_actual = datetime.date.today()
            reservas = Reserva.objects.filter(estado=True, usuario=request.user)
            for reserva in reservas :
                fecha_vencimiento = reserva.fecha_creacion + timedelta(days= 7)
                print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                print('Fecha Actual   ', fecha_actual, 'Fecha Vencimiento    ',fecha_vencimiento)
                if fecha_actual < fecha_vencimiento:
                    print(f'Fecha actual :{fecha_actual}')
                    print(f'Fecha creacion :{reserva.fecha_creacion}')
                    reserva.estado = False
                    reserva.save()
                    print(reserva, fecha_actual,"ggggg", reserva.estado)