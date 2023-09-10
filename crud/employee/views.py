from django.shortcuts import render
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
 
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
    employees = Employee.objects.all()  
    return render(request,"dados.html",{'employees':employees})  
def editar(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'editar.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/dados")  
    return render(request, 'editar.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/dados")