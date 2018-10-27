from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ItemDet

def index(request): 
	all_itemdets = ItemDet.objects.all()
	template = loader.get_template('sitee/index.html')
	context = {
			'all_itemdets': all_itemdets,

	}
	return HttpResponse(template.render(context, request))



def detail(request, ItemDet_id):
	return HttpResponse("<h2> details for item id: " + str(ItemDet_id)+ "</h2>")