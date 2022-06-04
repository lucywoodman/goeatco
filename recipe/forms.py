from django.forms import ModelForm, inlineformset_factory
from django.utils.translation import gettext_lazy as _
from cloudinary.forms import CloudinaryFileField
from .models import Category, Ingredient, IngredientMeta, Recipe, Instructions


class RecipeForm(ModelForm):
    featured_image = CloudinaryFileField(
        options={
            'crop': 'crop',
            'aspect_ratio': '16:9',
            'width': 1000,
            'folder': 'featured-images'
        }
    )

    class Meta:
        model = Recipe
        fields = ('public', 'name', 'description', 'meal',
                  'cooking_time', 'featured_image')
        exclude = ('slug', 'author')
        labels = {
            'name': _('Recipe name'),
            'cooking_time': _('Cooking time (in minutes)'),
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
