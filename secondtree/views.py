from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import ItemDet, User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

#Lekérdezi az adatbázisból a tárgyakat
def index(request): 
	all_itemdets = ItemDet.objects.all()
	return render(request, 'sitee/index.html', {'all_itemdets':all_itemdets})

def detail(request, ItemDet_id):
	try:
		item = ItemDet.objects.get(pk=ItemDet_id)
	except ItemDet.DoesNotExist:
		raise Http404("Item does not exist")
	return render(request, 'sitee/item.html', {'item':item})


class SignUp(generic.CreateView): #generic.CreateView :A view that displays a form for creating an object, redisplaying the form with validation errors (if there are any) and saving the object.
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'