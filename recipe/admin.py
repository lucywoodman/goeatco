from django.contrib import admin
from .models import Recipe, IngredientMeta

admin.site.register(Recipe)
admin.site.register(IngredientMeta)
