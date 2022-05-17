# Generated by Django 4.0.4 on 2022-05-15 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('diet', models.IntegerField(choices=[(0, ''), (1, 'Gluten free'), (2, 'Dairy free'), (3, 'Nut free'), (4, 'Soy free')], default=0)),
                ('source', models.URLField()),
                ('time', models.DurationField()),
                ('meal', models.IntegerField(choices=[(0, 'Breakfast'), (1, 'Lunch'), (2, 'Dinner'), (3, 'Snack'), (4, 'Other')], default=2)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]