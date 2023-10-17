from django import forms
from .models import Simulacion  

class SimulacionForm(forms.ModelForm):
    class Meta:
        model = Simulacion 
        fields = '__all__'#QUE DJNAGO INCLUYA LOS CAMPOS DEL MODELO SIMULACION