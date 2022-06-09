from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Ingredient, Category


class IngredientForm(ModelForm):
    """
    Class for the ingredient model form
    """
    class Meta:
        model = Ingredient
        fields = ('__all__')


class IngredientCategoryForm(ModelForm):
    """
    Class for the ingredient's category model form
    """
    class Meta:
        model = Ingredient
        fields = ('category',)
        labels = {
            'category': _('Filter ingredients by category'),
        }

    def __init__(self, *args, **kwargs):
        """
        Fetches the categories from the database to 
        list in the form's dropdown box
        """
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
