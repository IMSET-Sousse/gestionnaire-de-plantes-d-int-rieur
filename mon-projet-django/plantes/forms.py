from django import forms
from .models import Plante

class PlanteForm(forms.ModelForm):
    class Meta:
        model = Plante
        fields = ['nom', 'type_plante', 'date_plantation', 'arrosage_frequence', 'description']
