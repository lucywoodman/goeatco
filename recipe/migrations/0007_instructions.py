# Generated by Django 4.0.4 on 2022-05-22 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_remove_ingredient_recipe_ingredientmeta_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_no', models.PositiveSmallIntegerField()),
                ('description', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructions', to='recipe.recipe')),
            ],
        ),
    ]
