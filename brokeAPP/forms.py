# forms.py
from django import forms
from .models import Salario, Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['descripcion', 'fecha_vencimiento', 'direccion', 'actividad']  # Asegúrate de incluir fecha_vencimiento

# forms.py# forms.py

class SalarioForm(forms.ModelForm):
    tarea = forms.ModelChoiceField(queryset=Tarea.objects.all(), empty_label="Selecciona una tarea", required=True)

    class Meta:
        model = Salario
        fields = ['usuario', 'tarea', 'viaticos', 'pago_sitio', 'total']  # Agrega el campo tarea
    def clean_viaticos(self):
        viaticos = self.cleaned_data.get('viaticos', 0)
        return viaticos or 0  # Devuelve 0 si está vacío

    def clean_pago_sitio(self):
        pago_sitio = self.cleaned_data.get('pago_sitio', 0)
        return pago_sitio or 0  # Devuelve 0 si está vacío

    def clean_total(self):
        total = self.cleaned_data.get('total', 0)
        return total or 0  # Devuelve 0 si está vacío