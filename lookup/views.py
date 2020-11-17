from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lookup(request):
	return render(request, 'lookup.html')