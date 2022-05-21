from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    template_name = 'recipe/recipes.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})
