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
    path('<slug>/',            updat_form,         name='update'),
    path('<slug>/delete/',     employee_delete,    name='delete'),

]
