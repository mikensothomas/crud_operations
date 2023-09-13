from django.shortcuts import render
from django.shortcuts import render, redirect  
from app_empresa.forms import EmployeeForm  
from app_empresa.models import App_empresa  
 
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
    employee = App_empresa.objects.all()  
    return render(request,"dados.html",{'employee':employee})  
def editar(request, id):  
    employee = App_empresa.objects.get(id=id)  
    return render(request,'editar.html', {'employee':employee})  
def atualizar(request, id):  
    employee = App_empresa.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/dados")  
    return render(request, 'editar.html', {'employee': employee})  
def excluir(request, id):  
    employee = App_empresa.objects.get(id=id)  
    employee.delete()  
    return redirect("/dados")