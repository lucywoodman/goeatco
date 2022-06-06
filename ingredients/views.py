from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Ingredient
from .forms import IngredientForm, IngredientCategoryForm


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
    template_name = '_confirm_delete.html'
    success_url = reverse_lazy('ingredient_list')
