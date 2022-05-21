from django import forms
from django.forms import modelformset_factory
from .models import Recipe, Ingredient


class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', )
        labels = {
            'name': 'Recipe Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter recipe name here'
            }
            )
        }


IngredientFormset = modelformset_factory(
    Ingredient,
    fields=('name', ),
    extra=1,
    widgets={
        'name': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter ingredient here'
            }
        )
    }
)
