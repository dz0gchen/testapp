#coding: utf-8

from .models import Employees
from django.views.generic import TemplateView, ListView, DetailView

class Index(TemplateView):
    template_name = 'index.html'

#представление для вывода списка сотрудников с пагинацией    
class Catalog(ListView):    
    model = Employees
    paginate_by = 1
    context_object_name = 'catalog'   
    template_name = 'catalog.html'
    
    #переопределяем queryset для использования в разных случаях пагинации
    def get_queryset(self):
        query_string = ''
        #отслеживаем передачу параметров в форме
        if ('select' in self.request.GET) and self.request.GET['select'].strip():
            query_string = self.request.GET['select']
            
            #несколько избыточный код, но зато напрямую ничего из формы в запрос не вставляем
            if query_string == '1':
                queryset = Employees.objects.filter(beginning_of_work__isnull=False, end_of_work__isnull=True)
            else:
                queryset = Employees.objects.filter(beginning_of_work__isnull=False, end_of_work__isnull=False)
            #сохраняем параметр запроса в сессии для дальнейшего использования 
            self.request.session['paginate_by_select'] = query_string   
        else:
            #если была передача параметров в форме и задействован переход на страницу пагинации
            if self.request.session.get('paginate_by_select') and ('page' in self.request.GET):
                #queryset = Employees.objects.filter(department=self.request.session.get('paginate_by_department'))
                if self.request.session.get('paginate_by_select') == '1':
                    queryset = Employees.objects.filter(beginning_of_work__isnull=False, end_of_work__isnull=True)
                else:
                    queryset = Employees.objects.filter(beginning_of_work__isnull=False, end_of_work__isnull=False)
            #если форма не задействована 
            else:
                queryset = Employees.objects.all()
                if self.request.session.get('paginate_by_select'):
                    del self.request.session['paginate_by_select']

        return queryset
 
#представление для вывода детальной информации о сотруднике
class Employee(DetailView):
    model = Employees
    context_object_name = 'employee'
    template_name = 'employee.html'

    def get_object(self):
        obj = super(Employee, self).get_object()
        return obj

#представление для вывода алфавитного указателя    
class Pointer(ListView):
    surnames = []
    detail = []
    template_name = 'pointer.html'
    context_object_name = 'pointer'
    
    def get_queryset(self):
        
        self.detail[:] = []
        #отслеживаем передачу параметров в форме
        if 'params' in self.request.GET:
            params = self.request.GET['params']
            
            for letter in params:
            
                queryset = Employees.objects.filter(surname__istartswith=letter).iterator()
                
                for row in queryset:
                
                    self.detail.append(row)
         
        
        
         
        queryset = Employees.objects.order_by('surname').values('surname').iterator()
            
        for surnamedict in queryset:
             
            self.surnames.append(surnamedict['surname'])
                   
        return queryset
    
    #добавляем к контексту необходимую информацию    
    def get_context_data(self, **kwargs):
        
        letters = []
        groups = {}
        
        context = super(ListView, self).get_context_data(**kwargs)
        
        #формируем список букв
        for let in self.surnames:
            letters.append(let[0])
        
        #важно сохранить алфавитный порядок следования, такие способы не подходят
        #self.letters = list(set(self.letters))
        #self.letters = dict([(item, None) for item in self.letters]).keys()
        tmp = []
        for index, el in enumerate(letters):
            if el in letters[index + 1: ]:
                continue
            tmp.append(el)
            
        letters[:] = []
        letters = tmp
        del tmp
        
        count = len(letters)
        
        len_gr = 2.0
        count_gr = count / len_gr
        while count_gr > 7:
            len_gr += 1 
            count_gr = count / len_gr
        
        count_gr = int(count_gr)
        len_gr  = int(len_gr)
           
        #убираем остаток букв в последние группы   
        if count - len_gr * count_gr != 0:
            rez = count - len_gr * count_gr
            step = count_gr - rez 
        else:
            rez = None
     
        i = 0
        j = len_gr
        countw = 0          
        while count_gr:
            if rez:
                if countw == step:
                    j = j - len_gr
                    len_gr += 1
                    j = j + len_gr
                                        
            groups[countw] = ''.join(letters[i : j])
            i = i + len_gr
            j = j + len_gr
                        
            count_gr -= 1  
            countw += 1   
         
        context['dict'] = groups
        
        if len(self.detail) > 0:     
            context['detail'] = self.detail
            
        return context
    
    
    

    
    
    
#     #задание групп
#     groups = {u'А-Г': {u'А':[], u'Б':[], u'В':[], u'Г':[]},
#               u'Д-Ж': {u'Д':[],u'Е':[],u'Ё':[],u'Ж':[]},
#               u'З-К': {u'З':[],u'И':[],u'Й':[],u'К':[]},
#               u'Л-П': {u'Л':[],u'М':[],u'Н':[],u'О':[],u'П':[]},
#               u'Р-У': {u'Р':[],u'С':[],u'Т':[],u'У':[]},
#               u'Ф-Ч': {u'Ф':[],u'Х':[],u'Ц':[],u'Ч':[]},
#               u'Ш-Я': {u'Ш':[],u'Щ':[],u'Ъ':[],u'Ы':[],u'Ь':[],u'Э':[],u'Ю':[],u'Я':[]}}
#             
#     def get_queryset(self):
#         
#         queryset = Employees.objects.order_by('surname').values('surname').iterator()
#         
#         self.surnames[:] = []
#         for surnamequery in queryset:
#             
#             self.surnames.append(surnamequery['surname'])
#         
#          
#         for surname in self.surnames:
#             
#             #обходим группы
#             for group in self.groups.keys():
#                 
#                 #пробуем добавить в словарь группы значение для ключа буквы 
#                 try:
#                     self.groups[group][surname[0]][:] = []
#                     self.groups[group][surname[0]].append(surname)
#                 #если буквы ключа для первой буквы фамилии не существует, переходим к другой группе
#                 except KeyError:
#                     continue
#         
#         #обходим группы
#         for group in self.groups.keys():
#             
#             #обходим словари внутри группы
#             for key in self.groups[group].keys():
#                 
#                 #если список с фамилиями пустой, удаляем ключ-букву
#                 if len(self.groups[group][key]) == 0:
#                     del self.groups[group][key]
#             
#             #если после удаления ключей-букв в группе пустой список, т.е. нет фамилий для группы, удаляем группу 
#             if self.groups[group] == {}:
#                 del self.groups[group]
#                 
#         return queryset
#     
#     #добавляем к контексту необходимую информацию    
#     def get_context_data(self, **kwargs):
#         
#         context = super(ListView, self).get_context_data(**kwargs)
#         
#         context['groups'] = self.groups
#         
#         if u'А-Г' in self.request.GET:      
#             context['surnames'] = self.groups[u'А-Г']
#             
#         if u'Д-Ж' in self.request.GET:      
#             context['surnames'] = self.groups[u'Д-Ж']
#             
#         if u'З-К' in self.request.GET:      
#             context['surnames'] = self.groups[u'З-К']
#             
#         if u'Л-П' in self.request.GET:      
#             context['surnames'] = self.groups[u'Л-П']
#             
#         if u'Р-У' in self.request.GET:      
#             context['surnames'] = self.groups[u'Р-У']
#             
#         if u'Ф-Ч' in self.request.GET:      
#             context['surnames'] = self.groups[u'Ф-Ч']
#             
#         if u'Ш-Я' in self.request.GET:      
#             context['surnames'] = self.groups[u'Ш-Я']
#         
#         return context
            

        
        
        
        
    
    
    
    
    