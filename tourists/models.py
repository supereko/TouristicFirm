from django.db import models
import uuid

class Tourist(models.Model):
    """ Модель описывающая каждого туриста по отдельности  """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Уникальный номер каждого туриста')
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    date_of_arrival = models.DateField()
    date_of_departure = models.DateField()
    docs = models.FileField()
    note = models.TextField(max_length=1000, help_text='Примечание')
    STATUS = (
           ('r', 'заявка сформирована'),
           ('c', 'оплачено'),
    	   ('d', 'пакет документов готов'),
    	   ('h', 'заселен в отель'),
           ('e', 'на экскурсии'),
        )
	
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='r',
        help_text='Статус туриста',
    )
    #list_of_services = 
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
    #number_in_hotel = models.
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)
    excursion = models.ManyToManyField('excursion', help_text='Выберите экскурсии для туриста')
    
    def __str__(self):
        """ Функция, отображающая имя туриста """
        return self.name
		
    def display_excursion(self):
        """ Функция отображающая все экскурсии на которые записан турист"""
        return ', '.join(excursion.name for excours in self.excursion.all())	

class Hotel(models.Model):
    """ Модель описывающая отель для ттуристов  """  
    name = models.CharField(max_length=300, help_text='Введите название отеля')
    addres = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    cost_for_one_day = models.DecimalField(max_digits=7, decimal_places=2)
    check_in = models.TimeField()
    check_out = models.TimeField()

class Group(models.Model):
    """ Модель описывающая группы туристов  """
    manager =  models.CharField(max_length=200, help_text='Менеджер группы туристов') 
    STATUS = (
           ('r', 'сформирована'),
           ('e', 'на экскурсии'),
        )
	
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='r',
        help_text='Статус групп туристов',
    )
	  
class Excursion(models.Model):
    """ Модель описывающая экскурсии на которые записан турист"""
    name = models.CharField(max_length=300, help_text='Введите название экскурсии')
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    time_begin = models.TimeField()
    time_end = models.TimeField()
	
    def __str__(self):
        """ Функция отображающая название экскурсии"""
        return self.name