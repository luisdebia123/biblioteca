from django.forms import formset_factory
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Autor
from .forms import Autor_Form

class FormsetAutor(FormView):
    template_name = "app_libros/autor_formset.html"
    form_class = formset_factory(Autor_Form, extra = 1)
    success_url = reverse_lazy('app_libros:leer_autores')

    def form_valid(self, form):
        for f in form:
            if f.is_valid():
                f.save()
        return super().form_valid (form)
