# Generated by Django 4.0.4 on 2022-05-16 16:21

from django.db import migrations, models
import django.db.models.deletion
import recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_category_ingredient_unit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='unit',
        ),
        migrations.AddField(
            model_name='reciperequirement',
            name='unit',
            field=models.ManyToManyField(to='recipe.unit'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=recipe.models.LowerCaseField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=recipe.models.LowerCaseField(max_length=200, unique=True),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.reciperequirement'),
        ),
        migrations.RemoveField(
            model_name='reciperequirement',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='reciperequirement',
            name='ingredient',
            field=models.ManyToManyField(to='recipe.ingredient'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=recipe.models.LowerCaseField(max_length=30, unique=True),
        ),
    ]