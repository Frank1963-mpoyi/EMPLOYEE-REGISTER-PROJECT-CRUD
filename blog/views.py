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
    try:
        if request.method == "GET":
            form    = EmployeeForm()
            context =  {'form': form }
            return render (request, template_name, context )
        else:
            form    = EmployeeForm(request.POST or None)
            if form.is_valid():
                form.save()
            return redirect('blog:list')
    except:
        return redirect('blog:list')           
        
    
def updat_form (request, slug=None):
    template_name = 'blog/employee_form.html'
    try:
        obj     = get_object_or_404(Employee, slug=slug)
        form    = EmployeeForm(request.POST or None , instance=obj)
        if form.is_valid():
                form.save()
                return redirect('blog:list')
        context =  {'form': form }
        return render (request, template_name, context )
    except:
        return redirect('blog:list')    


def employee_delete (request, slug=None):
    template_name = 'blog/index.html'
    try:
        obj = get_object_or_404(Employee, slug=slug)
        obj.delete()
        return redirect('blog:list')
        #return redirect(employee_list)
    except:
        return redirect('blog:list') 