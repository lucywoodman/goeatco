from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

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

CATEGORY = (
    (0, 'other'),
    (1, 'vegetables'),
    (2, 'fruits'),
    (3, 'meat/fish'),
    (4, 'dairy'),
    (5, 'grains/legumes'),
    (6, 'herbs/spices'),
    (7, 'nuts/seeds/oils'),
    (8, 'stocks/condiments'),
)


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes')
    public = models.BooleanField(default=False)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    cooking_time = models.PositiveSmallIntegerField(default=0, blank=True)
    meal = models.IntegerField(choices=MEAL, default=2)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


def recipe_pre_save(instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.name)


pre_save.connect(recipe_pre_save, sender=Recipe)


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.IntegerField(choices=CATEGORY, default=0)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class IngredientMeta(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, related_name='meta', on_delete=models.CASCADE, null=True)
    recipe = models.ForeignKey(
        Recipe, related_name='ingredients', on_delete=models.CASCADE, null=True)
    qty = models.IntegerField()
    unit = models.IntegerField(choices=UNIT, default=0)

    def __str__(self):
        return f'{self.qty} {self.get_unit_display()} {self.ingredient}'


class Instructions(models.Model):
    recipe = models.ForeignKey(
        Recipe, related_name='instructions', on_delete=models.CASCADE, null=True)
    step = models.CharField(max_length=255)
