from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'email', 'phone', 'job_title', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Employee, EmployeeAdmin)
