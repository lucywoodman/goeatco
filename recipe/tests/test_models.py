from django.db import IntegrityError
from django.test import TestCase
from recipe.models import IngredientMeta, Recipe, Ingredient
import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class TestRecipeModel(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Set up a user and recipe for the tests
        cls.user = User.objects.create(
            username='test',
            email='test@test.com',
            password='super_secret_password',
        )

        cls.recipe = Recipe.objects.create(
            name='A test recipe',
            author=cls.user,
            cooking_time=datetime.timedelta(minutes=5),
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_recipe_has_an_author(self):
        """Recipes are correctly assigned a user"""
        recipe = self.recipe
        self.assertEqual(recipe.author.username, 'test')

    def test_recipe_has_slug(self):
        """Recipes are correctly given slugs when saving"""
        recipe = self.recipe
        self.assertEqual(recipe.slug, slugify(recipe.name))

    def test_recipe_has_unique_name(self):
        """Recipes raise an error if the name is not unique"""
        recipe1 = self.recipe
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
        recipe = self.recipe
        self.assertEqual(str(recipe), 'A test recipe')

    def test_recipe_meal_defaults_to_2(self):
        """Recipe meal defauls to choice 2: Dinner"""
        recipe = self.recipe
        self.assertEqual(recipe.meal, 2)

    def test_ingredient_string_returns_name(self):
        """Ingredient string returns the ingredient name"""
        ingredient = Ingredient.objects.create(
            name='A test ingredient'
        )
        self.assertEqual(str(ingredient), 'a test ingredient')

    def test_ingredient_name_converts_to_lowercase(self):
        """Ingredient string is lowercase"""
        ingredient = Ingredient.objects.create(
            name='A TEST INGREDIENT'
        )
        ingredient.save()
        self.assertEqual(ingredient.name, 'a test ingredient')


class TestIngredientMetaModel(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Set up a user, ingredient and recipe for the tests
        cls.user = User.objects.create(
            username='test',
            email='test@test.com',
            password='super_secret_password',
        )
        cls.ingredient = Ingredient.objects.create(
            name="A test ingredient"
        )
        cls.recipe = Recipe.objects.create(
            name='A test recipe',
            author=cls.user,
            cooking_time=datetime.timedelta(minutes=5),
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_ingredient_meta_string_returns_qty_unit_name(self):
        """Ingredient meta string returns qty, unit and name"""
        ingredient_meta = IngredientMeta.objects.create(
            qty="1",
            ingredient=self.ingredient,
            recipe=self.recipe,
        )
        self.assertEqual(str(ingredient_meta), f'1 item a test ingredient')
