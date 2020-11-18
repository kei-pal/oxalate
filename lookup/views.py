from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse

from .models import Ingredient

# Create your views here.
def lookup(request):
	return render(request, 'lookup.html')

def ingredient(request):
	ing_name = 'Spinach'
	ingredient = get_object_or_404(Ingredient, name=ing_name)

	context = {
		'name': ing_name,
		'source_notes': ingredient.source_notes,
		'ox_per_portion': ingredient.ox_per_portion,
		'portion_desc': ingredient.portion_desc,
		'portion_grams': ingredient.portion_grams,
		'alternatives': ingredient.alternatives,
	}
	return render(request, 'ingredient.html', context)