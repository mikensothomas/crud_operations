from django import forms  
from app_empresa.models import App_empresa
from django.forms import fields

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = App_empresa  
        fields = "__all__"  