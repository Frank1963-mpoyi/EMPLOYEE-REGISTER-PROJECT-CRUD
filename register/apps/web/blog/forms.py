from django                                         import forms

from .models                                        import Employee


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('fullname','mobile','empl_code','position')
        
        labels ={
            'fullname': 'Full Name',
            'empl_code': 'EMP. CODE'
            
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['empl_code'].required = False