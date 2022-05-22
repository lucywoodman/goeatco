from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from .models import Recipe, IngredientMeta
from .forms import RecipeForm, IngredientFormset


class RecipeList(ListView):
    model = Recipe
    template_name = 'recipe/recipe_list.html'


class RecipeDetail(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)

        return render(request, 'recipe/recipe_detail.html', {'recipe': recipe, })


class RecipeAdd(TemplateView):
    template_name = 'recipe/recipe_add.html'

    def get(self, *args, **kwargs):
        recipeform = RecipeForm()
        formset = IngredientFormset(queryset=IngredientMeta.objects.none())
        return self.render_to_response({
            'recipe_form': recipeform,
            'ingredient_formset': formset,
        })

    def post(self, request, *args, **kwargs):
        recipeform = RecipeForm(data=self.request.POST)
        formset = IngredientFormset(data=self.request.POST)
        if recipeform.is_valid() and formset.is_valid():
            recipe = recipeform.save()
            for form in formset:
                ingredient = form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()
            return redirect('recipe_list')

        return redirect('recipe_list')
