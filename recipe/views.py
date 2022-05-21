from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientFormset


class RecipeList(ListView):
    model = Recipe
    template_name = 'recipe/recipe_list.html'


class RecipeAdd(TemplateView):
    template_name = 'recipe/recipe_add.html'

    def get(self, *args, **kwargs):
        recipeform = RecipeForm(queryset=Recipe.objects.none())
        formset = IngredientFormset(queryset=Ingredient.objects.none())
        return self.render_to_response({'recipe_form': recipeform, 'ingredient_formset': formset})

    def post(self, *args, **kwargs):
        recipeform = RecipeForm(data=self.request.POST)
        formset = IngredientFormset(data=self.request.POST)
        if recipeform.is_valid() and formset.is_valid():
            recipe = recipeform.save()
            for form in formset:
                ingredient = form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()
            return redirect(reverse_lazy('recipe_list'))

        return self.render_to_response({'recipe_form': recipeform, 'ingredient_formset': formset})


class RecipeDetail(TemplateView):

    def get(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})
