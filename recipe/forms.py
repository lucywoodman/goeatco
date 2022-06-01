from django.forms import ModelForm, inlineformset_factory
from django.utils.translation import gettext_lazy as _
from .models import IngredientMeta, Recipe, Instructions


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('public', 'name', 'meal', 'cooking_time')
        exclude = ('slug', 'author')
        labels = {
            'name': _('Recipe name'),
        }


class IngredientForm(ModelForm):
    class Meta:
        model = IngredientMeta
        fields = ('__all__')


class InstructionForm(ModelForm):
    class Meta:
        model = Instructions
        fields = ('__all__')


IngredientFormset = inlineformset_factory(
    Recipe, IngredientMeta, form=IngredientForm, extra=1)
InstructionFormset = inlineformset_factory(
    Recipe, Instructions, form=InstructionForm, extra=1)
