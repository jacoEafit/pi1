from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def organizacion_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Verifica si el usuario tiene una instancia de 'Organizacion'
        if hasattr(request.user, 'organizacion'):
            return view_func(request, *args, **kwargs)
        else:
            # Redirige a una URL específica si el usuario no es de tipo organización
            return redirect('no_organizacion')
    return _wrapped_view


def sin_organizacion_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Verifica si el usuario no está autenticado
        if not request.user.is_authenticated:
            return redirect('login')  # Redirige a la página de login
        
        # Verifica si el usuario no tiene una organización asociada
        if not hasattr(request.user, 'organizacion'):
            return view_func(request, *args, **kwargs)
        
        # Redirige si el usuario tiene una organización
        return redirect('conOrganizacion')
    
    return _wrapped_view