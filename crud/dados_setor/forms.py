from django import forms  
from dados_setor.models import Dados_setor
from django.forms import fields

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Dados_setor  
        fields = "__all__"  