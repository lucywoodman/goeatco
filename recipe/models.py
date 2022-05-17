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


class LowerCaseField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCaseField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Unit(models.Model):
    name = LowerCaseField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = LowerCaseField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = LowerCaseField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class RecipeRequirement(models.Model):
    qty = models.DecimalField(max_digits=4, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.qty} {self.unit} {self.ingredient}'


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    diet = models.IntegerField(choices=DIET, default=0)
    source = models.URLField()
    cooking_time = models.DurationField()
    meal = models.IntegerField(choices=MEAL, default=2)
    ingredients = models.ManyToManyField(
        RecipeRequirement)
    instructions = models.TextField()

    def __str__(self):
        return self.title
