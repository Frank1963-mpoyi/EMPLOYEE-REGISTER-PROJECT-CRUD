from django.urls import path
from .views import (
    
    employee_list,  
    employee_form, 
    employee_delete,
    updat_form,
    
    )  



app_name = 'blog'

urlpatterns = [
    
    path('',                    employee_list,      name='list'  ),
    path('form',                employee_form,      name='form'  ),
    path('<str:slug>',            updat_form,         name='update'),
    path('<str:slug>/delete',     employee_delete,    name='delete'),

]
