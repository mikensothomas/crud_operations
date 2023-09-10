from django.shortcuts import render
from django.shortcuts import render, redirect  
from dados_setor.forms import EmployeeForm  
from dados_setor.models import Dados_setor
 
def salDados(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/dados')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def dados(request):  
    employees = Dados_setor.objects.all()  
    return render(request,"dados.html",{'employees':employees})  
def editar(request, id):  
    employee = Dados_setor.objects.get(id=id)  
    return render(request,'editar.html', {'dados_setor':employee})  
def atualizar(request, id):  
    dados_setor = Dados_setor.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = dados_setor)  
    if form.is_valid():  
        form.save()  
        return redirect("/dados")  
    return render(request, 'editar.html', {'dados_setor': dados_setor})  
def excluir(request, id):  
    dados_setor = Dados_setor.objects.get(id=id)  
    dados_setor.delete()  
    return redirect("/dados")