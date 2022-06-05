from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from .models import Ingredient, Recipe
from .forms import IngredientCategoryForm, IngredientForm, RecipeForm, IngredientFormset, InstructionFormset


class HomeListView(generic.ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        print(qs)
        query = self.request.GET.get('search')
        print(query)
        if self.request.user.is_authenticated:
            if query:
                qs = qs.filter(Q(name__icontains=query) |
                               Q(description__icontains=query))
            return qs
        else:
            qs = qs.filter(public=True)
            if query:
                qs = qs.filter(Q(name__icontains=query) |
                               Q(description__icontains=query))
            return qs


class RecipeDetailView(generic.DetailView):
    model = Recipe
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        saves_connected = get_object_or_404(
            Recipe, slug=self.kwargs.get('slug'))
        saved = False
        if saves_connected.saves.filter(id=self.request.user.id).exists():
            saved = True
        data['number_of_saves'] = saves_connected.number_of_saves()
        data['recipe_is_saved'] = saved
        return data


@login_required
def RecipeSave(request, slug):
    recipe = get_object_or_404(Recipe, slug=request.POST.get('recipe_save'))
    if recipe.saves.filter(id=request.user.id).exists():
        recipe.saves.remove(request.user)
    else:
        recipe.saves.add(request.user)

    return HttpResponseRedirect(reverse('recipe_detail', kwargs={'slug': slug}))


class RecipeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        data = super(RecipeCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormset(
                self.request.POST, self.request.FILES)
            data['instructions'] = InstructionFormset(
                self.request.POST, self.request.FILES)
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


class RecipeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        data = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormset(
                self.request.POST, self.request.FILES, instance=self.object)
            data['instructions'] = InstructionFormset(
                self.request.POST, self.request.FILES, instance=self.object)
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


class RecipeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe_list')


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('category')
        if query != None:
            return qs.filter(category__pk=query)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        context['form'] = IngredientCategoryForm()
        return context


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy('ingredient_list')


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy('ingredient_list')


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy('ingredient_list')


class CookbookView(LoginRequiredMixin, generic.ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipe/cookbook.html'

    def get_queryset(self):
        qs = super().get_queryset()
        query = qs.filter(saves__in=[self.request.user.id]).order_by('name')
        return query
