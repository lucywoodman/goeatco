# Generated by Django 3.2 on 2022-06-08 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['category', 'name']},
        ),
    ]
