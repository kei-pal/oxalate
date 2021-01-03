from django.urls import path
from . import views

urlpatterns = [
	path('about/', views.about, name='about'),
	path('FAQs/', views.faqs, name='faqs'),
	path('feedback/', views.feedback, name='feedback'),
	path('help/', views.help, name='help'),
]