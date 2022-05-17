from django.shortcuts import render
from django.views import generic
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    template_name = 'recipes.html'
    paginate_by = 6
