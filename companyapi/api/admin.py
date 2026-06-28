from django.contrib import admin
from .models import Company, Employee

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'company_id',
        'company_name',
        'company_location',
        'company_email',
        'type',
    )

    ordering = ('company_id',)
    
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = (
#         'company_id',
#         'company_name',
#         'company_location',
#         'company_email',
#         'type',
#     )

#     list_filter = (
#         'type',
#         'company_location',
#     )

#     search_fields = (
#         'company_name',
#         'company_email',
#         'company_location',
#     )
#     ordering = ('company_id',)



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee_id',
        'employee_name',
        'employee_email',
        'employee_phone',
        'employee_salary',
        'position',
        'company',
    )

    list_filter = (
        'position',
        'company',
    )

    search_fields = (
        'employee_name',
        'employee_email',
        'employee_phone',
        'employee_id',
    )