from django.db import models
from django.contrib.auth.models import User

MEAL = (
    (0, 'Breakfast'),
    (1, 'Lunch'),
    (2, 'Dinner'),
    (3, 'Snack'),
    (4, 'Other'),
)


class LowerCaseField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCaseField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes')
    cooking_time = models.DurationField()
    meal = models.IntegerField(choices=MEAL, default=2)

    def __str__(self):
        return self.name

    def get_ingredients(self):
        return self.ingredients.all()


class Ingredient(models.Model):
    name = LowerCaseField(max_length=200, unique=True)
    recipe = models.ForeignKey(
        Recipe, related_name='ingredients', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
