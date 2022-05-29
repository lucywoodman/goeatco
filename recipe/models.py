from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify

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
    (4, 'ml'),
)


class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes')
    cooking_time = models.DurationField()
    meal = models.IntegerField(choices=MEAL, default=2)

    def __str__(self):
        return self.name

    def get_ingredients(self):
        return self.ingredients.all()


def recipe_pre_save(instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.name)


pre_save.connect(recipe_pre_save, sender=Recipe)


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class IngredientMeta(models.Model):
    qty = models.IntegerField()
    unit = models.IntegerField(choices=UNIT, default=0)
    ingredient = models.ForeignKey(
        Ingredient, related_name='meta', on_delete=models.CASCADE, null=True)
    recipe = models.ForeignKey(
        Recipe, related_name='ingredients', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.qty} {self.get_unit_display()} {self.ingredient}'


class Instructions(models.Model):
    step = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe, related_name='instructions', on_delete=models.CASCADE, null=True)
