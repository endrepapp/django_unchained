from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'), # main site load
    path('<int:ItemDet_id>/', views.detail, name='detail'), # adott oldalt nyitja meg részletes leírással.
    path('signup/', views.SignUp.as_view(), name='signup'),
]
