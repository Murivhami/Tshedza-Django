# Generated by Django 5.1.7 on 2025-04-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FitFair', '0005_alter_meal_meal_of_the_day_alter_meal_total_calories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(),
        ),
    ]
