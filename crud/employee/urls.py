from django.contrib import admin  
from django.urls import path  
from employee import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('salDados', views.salDados),  
    path('dados',views.dados),  
    path('editar/<int:id>', views.editar),  
    path('atualizar/<int:id>', views.atualizar),  
    path('excluir/<int:id>', views.excluir),  
]  