from django.urls import path  
from app_empresa import views  

urlpatterns = [  
    path('salDados', views.salDados),  
    path('dados',views.dados),  
    path('editar/<int:id>', views.editar),  
    path('atualizar/<int:id>', views.atualizar),  
    path('excluir/<int:id>', views.excluir),  
]  