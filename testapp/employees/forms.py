#coding:utf-8

from django import forms
from .models import Employees

class EmployeesForm(forms.ModelForm):
    
    #настройка, определяющая модель для формы
    class Meta:
        model = Employees
        fields = ['name', 'surname', 'middle_name', 'date_of_birth', 'email', 'phonenumber', 'beginning_of_work', 'end_of_work', 'position', 'department'] 
        
class EmployeesFormForAddButton(forms.ModelForm):
    
    #настройка, определяющая модель для формы при добавлении сотрудника в админке
    class Meta:
        model = Employees
        fields = ['name', 'surname', 'middle_name', 'date_of_birth', 'email', 'phonenumber', 'beginning_of_work', 'position', 'department']