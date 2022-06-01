from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.db import transaction
from .models import Recipe, IngredientMeta, Instructions
from .forms import RecipeForm, IngredientFormset, InstructionFormset


class SuccessView(generic.TemplateView):
    template_name = 'recipe/success.html'


class RecipeListView(generic.ListView):
    model = Recipe
    context_object_name = 'recipes'


class RecipeDetailView(generic.DetailView):
    model = Recipe
    context_object_name = 'recipe'


class RecipeCreateView(generic.CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = 'success/'

    def get_context_data(self, **kwargs):
        data = super(RecipeCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormset(self.request.POST)
            data['instructions'] = InstructionFormset(self.request.POST)
        else:
            data['ingredients'] = IngredientFormset()
            data['instructions'] = InstructionFormset()
        return data

    def form_valid(self, form):
        form.instance.author = self.request.user
        context = self.get_context_data()
        ingredients = context['ingredients']
        instructions = context['instructions']
        with transaction.atomic():
            self.object = form.save()

            if ingredients.is_valid() and instructions.is_valid():
                ingredients.instance = self.object
                instructions.instance = self.object
                ingredients.save()
                instructions.save()
        return super(RecipeCreateView, self).form_valid(form)


class RecipeUpdateView(generic.UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = '_update_form'
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormset(
                self.request.POST, instance=self.object)
            data['instructions'] = InstructionFormset(
                self.request.POST, instance=self.object)
        else:
            data['ingredients'] = IngredientFormset(instance=self.object)
            data['instructions'] = InstructionFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        instructions = context['instructions']
        with transaction.atomic():
            self.object = form.save()

            if ingredients.is_valid() and instructions.is_valid():
                ingredients.instance = self.object
                instructions.instance = self.object
                ingredients.save()
                instructions.save()
        return super(RecipeUpdateView, self).form_valid(form)


class RecipeDeleteView(generic.DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe_list')
