
from django import forms
from .models import Nouveau

class NouveauForm(forms.ModelForm):
    class Meta:
        model = Nouveau
        fields = '__all__'

class Data_uploadForm(forms.Form):
    file = forms.FileField()
   


