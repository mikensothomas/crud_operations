from django.db import models  
class Employee(models.Model):  
    nome_setor = models.CharField(max_length=30)  
    funcionarios = models.IntegerField(blank=True, null=True)  
    fornecedores = models.IntegerField(blank=True, null=True)  
    produtos = models.IntegerField(blank=True, null=True)
    empresa_terceira = models.IntegerField(blank=True, null=True) 

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee"  