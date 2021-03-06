from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from ingredients.models import Ingredient

MEAL = (
    (0, 'Breakfast'),
    (1, 'Lunch'),
    (2, 'Dinner'),
    (3, 'Snack'),
    (4, 'Other'),
)

UNIT = (
    (0, 'item'),
    (1, 'g'),
    (2, 'kg'),
    (3, 'cups'),
    (4, 'tsp'),
    (5, 'tbsp'),
)


class Recipe(models.Model):
    """
    Class for the recipe model
    FK - User model (author)
    M:M - User model (saves)
    """
    class Meta:
        ordering = ['name']

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes')
    public = models.BooleanField(default=False)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.CharField(max_length=500)
    cooking_time = models.PositiveSmallIntegerField(default=0, blank=True)
    meal = models.IntegerField(choices=MEAL, default=2)
    featured_image = CloudinaryField('image', default='placeholder')
    saves = models.ManyToManyField(
        User, related_name='recipe_saves', blank=True)

    def __str__(self):
        return self.name

    def number_of_saves(self):
        return self.saves.count()


def recipe_pre_save(instance, *args, **kwargs):
    """
    Saves the recipe name as a slug before saving the recipe
    """
    if instance.slug is None:
        instance.slug = slugify(instance.name)


pre_save.connect(recipe_pre_save, sender=Recipe)


class IngredientMeta(models.Model):
    """
    Class for the ingredient meta model
    This model is an interrim model between recipe and ingredient
    FK - Ingredient model (ingredient)
    FK - Recipe model (recipe)
    """
    ingredient = models.ForeignKey(
        Ingredient, related_name='meta', on_delete=models.CASCADE, null=True)
    recipe = models.ForeignKey(
        Recipe,
        related_name='ingredients',
        on_delete=models.CASCADE,
        null=True)
    qty = models.IntegerField()
    unit = models.IntegerField(choices=UNIT, default=0)

    def __str__(self):
        return f'{self.qty} {self.get_unit_display()} {self.ingredient}'


class Instructions(models.Model):
    """
    Class for the instructions model
    FK - Recipe model (recipe)
    """
    recipe = models.ForeignKey(
        Recipe,
        related_name='instructions',
        on_delete=models.CASCADE,
        null=True)
    step = models.CharField(max_length=255)
