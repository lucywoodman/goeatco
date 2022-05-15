from django.db import models
from django.contrib.auth.models import User

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
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes')
    diet = models.IntegerField(choices=DIET, default=0)
    source = models.URLField()
    time = models.DurationField()
    meal = models.IntegerField(choices=MEAL, default=2)
    content = models.TextField()

    def __str__(self):
        return self.title
