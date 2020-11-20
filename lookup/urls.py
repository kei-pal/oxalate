from django.urls import path
from . import views

urlpatterns = [
	path('', views.lookup, name='lookup'),
	path('ingr/<ingr_name>/', views.ingredient, name='ingredient'),
	path('meal/<meal_name>/', views.meal, name='meal')
]