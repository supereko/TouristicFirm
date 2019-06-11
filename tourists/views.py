from django.shortcuts import render
from tourists.models import Tourist, Hotel, Group, Excursion


def index(request):
    """Вью главной страницы"""

    # Вычисляем общее количество туристов
    num_tourists = Tourist.objects.all().count()
    
    # Количество туристов, подавших заявки
    num_tour_req = Tourist.objects.filter(status__exact='r').count()
	
	# Количество туристов, готовых к приёму (с готовыми документами)
    num_tour_ready = Tourist.objects.filter(status__exact='d').count()
	
	# Количество сформированных групп
    num_group = Group.objects.all().count()
	
    context = {
	    'num_tourists': num_tourists, 
		'num_tour_req': num_tour_req,
		'num_tour_ready': num_tour_ready,
		'num_group': num_group
		}

    # Передаём HTML шаблону index.html данные контекста
    return render(request, 'index.html', context=context)
