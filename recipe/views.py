from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from .models import Recipe, IngredientMeta, Instructions
from .forms import RecipeForm, IngredientFormset, InstructionFormset


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
        ingredient_formset = IngredientFormset(
            queryset=IngredientMeta.objects.none())
        instructions_formset = InstructionFormset(
            queryset=Instructions.objects.none())
        return self.render_to_response({
            'recipe_form': recipeform,
            'ingredient_formset': ingredient_formset,
            'instructions_formset': instructions_formset,
        })

    def post(self, request, *args, **kwargs):
        recipeform = RecipeForm(data=self.request.POST)
        ingredient_formset = IngredientFormset(data=self.request.POST)
        instructions_formset = InstructionFormset(data=self.request.POST)
        if recipeform.is_valid() and ingredient_formset.is_valid() and instructions_formset.is_valid():
            recipe = recipeform.save()
            for form in ingredient_formset:
                ingredient = form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()
            for form in instructions_formset:
                instruction = form.save(commit=False)
                instruction.recipe = recipe
                instruction.save()
            return redirect('recipe_list')

        return redirect('recipe_list')
