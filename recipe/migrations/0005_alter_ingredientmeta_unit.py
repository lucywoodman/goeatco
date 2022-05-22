# Generated by Django 4.0.4 on 2022-05-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_ingredientmeta_alter_ingredient_recipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientmeta',
            name='unit',
            field=models.IntegerField(choices=[(0, 'item'), (1, 'g'), (2, 'kg'), (3, 'cups'), (4, 'ml')], default=0),
        ),
    ]