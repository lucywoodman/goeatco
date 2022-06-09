from django.db import models


class Category(models.Model):
    """
    Class for the category model
    Used to categorise the ingredients
    """
    name = models.CharField(max_length=80, unique=True)

    def save(self, *args, **kwargs):
        """
        Converts the category name to lowercase on save
        """
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """
    Class for the ingredient model
    FK - Category model (category)
    """
    class Meta:
        ordering = ['category', 'name']

    name = models.CharField(max_length=80, unique=True)
    category = models.ForeignKey(
        Category, related_name='ingredients', on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        """
        Converts the ingredient name to lowercase on save
        """
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
