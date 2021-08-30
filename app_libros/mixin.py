from django.shortcuts import redirect

class Super_Usuario_Mixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return redirect('app_libros:home')       