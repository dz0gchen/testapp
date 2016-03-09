#coding: utf-8

from __future__ import unicode_literals
from django.db import models
#easy_install django-phonenumber-field
from phonenumber_field.modelfields import PhoneNumberField

class Employees(models.Model):
        
    name = models.CharField(u'имя', max_length=120, blank=False, null=False)
    surname = models.CharField(u'фамилия', max_length=120, blank=False, null=False)
    middle_name = models.CharField(u'отчество', max_length=120, blank=False, null=False)
    date_of_birth = models.DateField(u'дата рождения', auto_now_add=False, auto_now=False)
    email = models.EmailField(u'электронная почта')
    phonenumber = PhoneNumberField(u'телефон')
    beginning_of_work = models.DateField(u'начало работы', auto_now_add=False, auto_now=False)
    end_of_work = models.DateField(u'заверешение работы', blank=True, null=True, auto_now_add=False, auto_now=False)
    position = models.CharField(u'должность', max_length=100, blank=False, null=False)
    department = models.CharField(u'отдел', max_length=100, blank=False, null=False)
        
    def __unicode__(self): 
        #возращает поля, которые отображаются после добавления в админке
        return '%s %s %s %s %s %s %s %s %s %s' % (self.name, self.surname, self.middle_name, 
                          self.date_of_birth, self.email, self.phonenumber, self.beginning_of_work, 
                          self.end_of_work, self.position, self.department)