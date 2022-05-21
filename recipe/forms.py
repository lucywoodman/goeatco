from django.forms import ModelForm, modelformset_factory
from .models import Recipe, Ingredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'meal')


IngredientFormset = modelformset_factory(
    Ingredient, fields=('name', ), extra=1
)
