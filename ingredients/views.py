from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Ingredient
from .forms import IngredientForm, IngredientCategoryForm


class IngredientListView(LoginRequiredMixin, generic.ListView):
    """
    Class for ingredient list page
    Lists all ingredients in a table format
    """
    model = Ingredient

    def get_queryset(self):
        """
        Fetches the selected category from the sidebar form
        Filters the queryset by the category's primary key
        """
        qs = super().get_queryset()
        query = self.request.GET.get('category')
        if query != None:
            return qs.filter(category__pk=query)
        else:
            return qs

    def get_context_data(self, **kwargs):
        """
        Context for the sidebar form
        """
        context = super(IngredientListView, self).get_context_data(**kwargs)
        context['form'] = IngredientCategoryForm()
        return context


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Class for creating new ingredients
    Returns to ingredient list after submission
    """
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy('ingredient_list')


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    Class for updating existing ingredients
    Returns to ingredient list after submission
    """
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy('ingredient_list')


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    Class for deleting existing ingredients
    Displays the deletion confirmation page before returning
    to the ingredient list
    """
    model = Ingredient
    template_name = '_confirm_delete.html'
    success_url = reverse_lazy('ingredient_list')
