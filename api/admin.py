from django.contrib import admin
from api.models import Company, Employee

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name', 'location', 'type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone', 'about', 'position', 'company')
    list_filter = ('position', 'company')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)