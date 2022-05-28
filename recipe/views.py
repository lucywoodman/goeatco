from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic, View
from .models import Recipe, IngredientMeta, Instructions
from .forms import RecipeForm, IngredientFormset, InstructionFormset


class RecipeList(generic.ListView):
    model = Recipe
    template_name = 'recipe/recipe_list.html'


class RecipeDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'recipe/recipe_detail.html',
            {
                'recipe': recipe,
            })


class RecipeAdd(View):
    def get(self, request, *args, **kwargs):
        recipe_form = RecipeForm()
        ingredient_formset = IngredientFormset(
            queryset=IngredientMeta.objects.none())
        instruction_formset = InstructionFormset(
            queryset=Instructions.objects.none())

        return render(
            request,
            'recipe/recipe_add.html',
            {
                'recipe_form': recipe_form,
                'ingredient_formset': ingredient_formset,
                'instruction_formset': instruction_formset,
            })

    def post(self, request, *args, **kwargs):
        recipe_form = RecipeForm(data=request.POST)
        ingredient_formset = IngredientFormset(data=request.POST)
        instruction_formset = InstructionFormset(data=request.POST)

        if recipe_form.is_valid() and ingredient_formset.is_valid() and instruction_formset.is_valid():
            recipe_form.instance.author = request.user
            recipe = recipe_form.save(commit=False)
            recipe.save()
            for form in ingredient_formset:
                ingredient = form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()
            for form in instruction_formset:
                instruction = form.save(commit=False)
                instruction.recipe = recipe
                instruction.save()
        else:
            recipe_form = RecipeForm()

        return redirect('recipe_list')
