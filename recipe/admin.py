from django.contrib import admin
from .models import Recipe, Ingredient, IngredientMeta


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientMeta)
