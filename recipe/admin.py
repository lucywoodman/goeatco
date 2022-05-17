from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Unit, Category, Ingredient, RecipeRequirement


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'meal', 'cooking_time')
    search_fields = ['title', 'ingredients', 'instructions']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('diet', 'meal', 'cooking_time')
    summernote_fields = ('instructions')
    autocomplete_fields = ['ingredients']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ['name']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Unit)
admin.site.register(Category)


@admin.register(RecipeRequirement)
class RecipeRequirementAdmin(admin.ModelAdmin):
    search_fields = ['ingredient']
    autocomplete_fields = ['ingredient']
