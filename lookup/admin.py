from django.contrib import admin
from .models import Ingredient, Meal, MealIngredient

# Register your models here.
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Ingredient)
admin.site.register(Meal)
admin.site.register(MealIngredient)

@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    ordering = ['name']
    pass

# class ViewAdmin(ImportExportModelAdmin):
#     pass