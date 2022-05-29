from django.test import TestCase
from recipe.models import Recipe
import datetime
from django.contrib.auth.models import User


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
