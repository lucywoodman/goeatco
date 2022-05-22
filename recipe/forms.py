from django.forms import ModelForm, modelformset_factory
from django.utils.translation import gettext_lazy as _
from .models import IngredientMeta, Recipe, Instructions


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'slug', 'author', 'meal', 'cooking_time')
        labels = {
            'name': _('Recipe name'),
        }


IngredientFormset = modelformset_factory(
    IngredientMeta, fields=('qty', 'unit', 'ingredient'), extra=1)
InstructionFormset = modelformset_factory(
    Instructions, fields=('step_no', 'description'), extra=1)
