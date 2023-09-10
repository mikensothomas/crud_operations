from django.contrib import admin  
from django.urls import path  
from employee import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('salDados', views.salDados),  
    path('dados',views.dados),  
    path('editar/<int:id>', views.editar),  
    path('update/<int:id>', views.atualizar),  
    path('delete/<int:id>', views.excluir),  
]  