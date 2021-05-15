from  django.shortcuts  import render,       redirect,  get_object_or_404
from  .forms            import EmployeeForm
from  .models           import Employee






def employee_list (request):
    template_name = 'blog/employee_list.html'
    employee_list = Employee.objects.all()
    context = {'employee_list': employee_list}
    return render (request, template_name, context)




def employee_form (request):
    template_name      = 'blog/employee_form.html'
    if request.method == "GET":
        form    = EmployeeForm()
        context =  {'form': form }
        return render (request, template_name, context )
    else:
        form    = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('blog:list')
        
        
    
def updat_form (request, pk=None):
    template_name = 'blog/employee_form.html'
    obj     = get_object_or_404(Employee, pk=pk)
    form    = EmployeeForm(request.POST or None , instance=obj)
    if form.is_valid():
            form.save()
            return redirect('blog:list')# can also redirect to the views function 
    context =  {'form': form }
    return render (request, template_name, context )



def employee_delete (request, pk=None):
    template_name = 'blog/index.html'
    obj = get_object_or_404(Employee, id=pk)
    obj.delete()
    return redirect('blog:list')
    #return redirect(employee_list)
