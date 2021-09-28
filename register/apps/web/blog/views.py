from django.contrib                                         import messages
from django.contrib.auth.decorators                         import login_required
from django.shortcuts                                       import render, redirect, get_object_or_404

from .forms                                                 import EmployeeForm
from .models                                                import Employee


@login_required
def employee_list (request):
    template_name       = 'apps/blog/employee_list.html'

    employee_list       = Employee.objects.all()

    context             = {
        'employee_list': employee_list
        }

    return render (request, template_name, context)


@login_required
def employee_form (request):
    template_name            = 'apps/blog/employee_form.html'

    form    = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "The form was submitted successfully.")

        return redirect(request.META['HTTP_REFERER'])

    context = { 'form': form }

    return render(request, template_name, context)


@login_required
def updat_form(request, slug=None):
    template_name = 'apps/blog/employee_form.html'

    obj     = get_object_or_404(Employee, slug=slug)

    form    = EmployeeForm(request.POST or None , instance=obj)

    if form.is_valid():
        form.save()

        messages.success(request, "The form is update successfully.")
        return redirect('blog:list')

    context =  {'form': form }
    return render (request, template_name, context )


def employee_delete (request, slug=None):

    obj = get_object_or_404(Employee, slug=slug)
    obj.delete()

    messages.success(request, "The record is deleted successfully .")
    return redirect('blog:list')
