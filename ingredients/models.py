from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=80, unique=True)
    category = models.ForeignKey(
        Category, related_name='categories', on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
