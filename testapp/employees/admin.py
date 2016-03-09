#coding:utf-8

from django.contrib import admin
from .models import Employees
from .forms import EmployeesForm, EmployeesFormForAddButton

#детализации вывода информации по полям модели в админке при редактировании записи
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'middle_name', 'position', 'department', 'phonenumber']
    form = EmployeesForm
    
    #подставляем разные формы для действия "редактировать" и "добавить"
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = EmployeesForm
        else:
            self.form = EmployeesFormForAddButton
        return super(EmployeesAdmin, self).get_form(request, obj, **kwargs)
    
admin.site.register(Employees, EmployeesAdmin)