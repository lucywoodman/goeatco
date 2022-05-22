from django.forms import ModelForm, modelformset_factory
from django.utils.translation import gettext_lazy as _
from .models import IngredientMeta, Recipe, Ingredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'slug', 'author', 'meal', 'cooking_time')
        labels = {
            'name': _('Recipe name'),
        }


IngredientFormset = modelformset_factory(Ingredient, fields=('name',), extra=1)
IngredientMetaFormset = modelformset_factory(
    IngredientMeta, fields=('qty', 'unit'), extra=1)
