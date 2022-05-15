from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Unit, Category, Ingredient, RecipeRequirement


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('instructions')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Unit)
admin.site.register(Category)
admin.site.register(RecipeRequirement)
