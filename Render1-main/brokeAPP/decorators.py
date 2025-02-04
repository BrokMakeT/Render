from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol == 'Admin':
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'Acceso denegado. Debes ser administrador para acceder a esta página.')
            return redirect('home')  # Redirige al login o a otra vista si no es admin
    return _wrapped_view

def empleado_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol == 'Empleado':
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'Acceso denegado. Solo los empleados pueden acceder a esta página.')
            return redirect('home')  # Redirige al login o a otra vista si no es empleado
    return _wrapped_view