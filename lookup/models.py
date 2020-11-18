from django.db import models

# Create your models here.
class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	portion_desc = models.CharField(max_length=50)
	portion_grams = models.IntegerField()
	alternatives = models.CharField(max_length=200)
	ox_per_100g = models.DecimalField(max_digits=5, decimal_places=2)
	source_notes = models.TextField()

	def __str__(self):
		return self.name

	@property
	def ox_per_portion(self):
		return self.portion_grams * (self.ox_per_100g / 100)