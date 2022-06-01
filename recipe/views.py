from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
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

    def get(self, *args, **kwargs):
        # clear reference to self
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormset()
        instruction_form = InstructionFormset()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                ingredient_form=ingredient_form,
                instruction_form=instruction_form
            )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormset(self.request.POST)
        instruction_form = InstructionFormset(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid() and
                instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        form.instance.author = self.request.user
        self.object = form.save()
        for item in ingredient_form:
            item.recipe = self.object
            item.save()
        for item in instruction_form:
            item.recipe = self.object
            item.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form, instruction_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))


class RecipeUpdateView(generic.UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = '_update_form'
    success_url = '/'

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormset(instance=self.object)
        instruction_form = InstructionFormset(instance=self.object)
        return self.render_to_response(
            self.get_context_data(
                form=form,
                ingredient_form=ingredient_form,
                instruction_form=instruction_form
            )
        )

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormset(
            self.request.POST, instance=self.object)
        instruction_form = InstructionFormset(
            self.request.POST, instance=self.object)

        if (form.is_valid() and ingredient_form.is_valid() and
                instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form, instruction_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))


class RecipeDeleteView(generic.DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe_list')
