from django.forms import ModelForm, modelformset_factory
from django.utils.translation import gettext_lazy as _
from .models import IngredientMeta, Recipe, Instructions


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'meal', 'cooking_time')
        exclude = ('slug', 'author')
        labels = {
            'name': _('Recipe name'),
        }


IngredientFormset = modelformset_factory(
    IngredientMeta, fields=('qty', 'unit', 'ingredient'), extra=1)
InstructionFormset = modelformset_factory(
    Instructions, fields=('step', ), extra=1)
