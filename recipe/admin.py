from django.contrib import admin
from .models import Category, Recipe, Ingredient, IngredientMeta


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientMeta)
admin.site.register(Category)
