from django.db import IntegrityError
from django.test import TestCase
from recipe.models import Recipe, Ingredient
import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class TestModels(TestCase):

    def setUp(self):
        # Set up a user for the tests
        self.user = User.objects.create(
            username='test',
            email='test@test.com',
            password='super_secret_password',
        )

    def test_recipe_has_an_author(self):
        """Recipes are correctly assigned a user"""
        recipe = Recipe.objects.create(
            name='A test recipe',
            author=self.user,
            cooking_time=datetime.timedelta(minutes=5),
        )
        self.assertEqual(recipe.author.username, 'test')

    def test_recipe_has_slug(self):
        """Recipes are correctly given slugs when saving"""
        recipe = Recipe.objects.create(
            name='A test recipe',
            author=self.user,
            cooking_time=datetime.timedelta(minutes=5),
        )
        self.assertEqual(recipe.slug, slugify(recipe.name))

    def test_recipe_has_unique_name(self):
        """Recipes raise an error if the name is not unique"""
        recipe1 = Recipe.objects.create(
            name='A test recipe',
            author=self.user,
            cooking_time=datetime.timedelta(minutes=5),
        )
        recipe1.save()
        with self.assertRaises(IntegrityError):
            recipe2 = Recipe.objects.create(
                name='A test recipe',
                author=self.user,
                cooking_time=datetime.timedelta(minutes=5),
            )
            recipe2.save()

    def test_recipe_string_returns_name(self):
        """Recipe string returns the recipe name"""
        recipe = Recipe.objects.create(
            name='A test recipe',
            author=self.user,
            cooking_time=datetime.timedelta(minutes=5),
        )
        self.assertEqual(str(recipe), 'A test recipe')

    def test_recipe_meal_defaults_to_2(self):
        """Recipe meal defauls to choice 2: Dinner"""
        recipe = Recipe.objects.create(
            name='A test recipe',
            author=self.user,
            cooking_time=datetime.timedelta(minutes=5),
        )
        self.assertEqual(recipe.meal, 2)

    def test_ingredient_string_returns_name(self):
        """Ingredient string returns the ingredient name"""
        ingredient = Ingredient.objects.create(
            name='A test ingredient'
        )
        self.assertEqual(str(ingredient), 'A test ingredient')
