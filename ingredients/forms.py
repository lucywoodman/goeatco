from django.forms import ModelForm
from .models import Ingredient, Category


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('__all__')


class IngredientCategoryForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('category',)
        labels = {
            'category': _('Filter ingredients by category'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
