from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('<int:ItemDet_id>/', views.detail, name='detail'),
    
]
