from django.urls import path
from . import views

urlpatterns = [
	path('', views.lookup, name='lookup'),
	path('i/<ingr_name>/', views.ingredient, name='ingredient'),
	path('m/<meal_name>/', views.meal, name='meal')
]