# Generated by Django 4.0.4 on 2022-05-21 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recipe.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('cooking_time', models.DurationField()),
                ('meal', models.IntegerField(choices=[(0, 'Breakfast'), (1, 'Lunch'), (2, 'Dinner'), (3, 'Snack'), (4, 'Other')], default=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', recipe.models.LowerCaseField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredients', to='recipe.recipe')),
            ],
        ),
    ]
