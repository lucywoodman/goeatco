from django.db import models

DIET = (
    (0, ''),
    (1, 'Gluten free'),
    (2, 'Dairy free'),
    (3, 'Nut free'),
    (4, 'Soy free'),
)

MEAL = (
    (0, 'Breakfast'),
    (1, 'Lunch'),
    (2, 'Dinner'),
    (3, 'Snack'),
    (4, 'Other'),
)


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    diet = models.IntegerField(choices=DIET, default=0)
    source = models.URLField()
    cooking_time = models.DurationField()
    meal = models.IntegerField(choices=MEAL, default=2)

    instructions = models.TextField()

    def __str__(self):
        return self.title


class Unit(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default={name})
    unit = models.ForeignKey(
        Unit, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
