from    django.contrib      import admin
from    .models             import Position, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'empl_code', 'mobile','position'] #,'slug'
    list_filter = ['position']

admin.site.register(Position)

