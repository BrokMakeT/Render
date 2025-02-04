from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', TemplateView.as_view(template_name='brokeapp1/index.html'), name='home'),  # Ruta para index.html
    path('loginAdmin/', TemplateView.as_view(template_name='brokeapp1/loginAdmin.html'), name='loginAdmin'),  # Ruta para loginAdmin.html
    path('loginUser/', TemplateView.as_view(template_name='brokeapp1/loginUser.html'), name='loginUser'),  # Ruta para loginUser.html
    path('', include('brokeAPP.urls')),  # Incluye las URLs de brokeAPP que necesiten ser autentificadas 

]
