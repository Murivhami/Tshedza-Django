<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

#Model for storing user details.
=======
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.db.models import Sum

#User model for storing user details.
>>>>>>> 16526d6 (Project Setup, app creation, Models, and serializers creation)
class CustomUser(AbstractUser):
    CITY_CHOICES = [
        ('JHB', 'Johannesburg'),
        ('CPT', 'Cape Town'),
        ('DBN', 'Durban'),
        ('PTA', 'Pretoria'),
        ('BFN', 'Bloemfontein'),
        ('PLZ', 'Port Elizabeth'),
        ('EL', 'East London'),
        ('PLK', 'Polokwane'),
        ('NLP', 'Nelspruit'),
        ('KIM', 'Kimberley'),
        ('RST', 'Rustenburg'),
        ('PMB', 'Pietermaritzburg')
    ]
<<<<<<< HEAD
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, choices=CITY_CHOICES, null=True, blank=False)
    
=======
    age = models.PositiveIntegerField(null=False, blank=False)
    location = models.CharField(max_length=255, choices=CITY_CHOICES, null=False, blank=False)
>>>>>>> 16526d6 (Project Setup, app creation, Models, and serializers creation)

    def __str__(self):
        return self.username

<<<<<<< HEAD
#Model for storing the meal details for a user.
class Meal(models.Model):
    user= models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    MEALTYPE_CHOICES = [
    ('breakfast', 'breakfast'),
    ('lunch', 'lunch'),
    ('dinner', 'dinner'),
    ('snack', 'snack')
    ]
    meal_of_the_day = models.CharField(max_length=255,choices=MEALTYPE_CHOICES, null=True, blank=True)
    food_item = models.CharField(max_length=255, null=True, blank=True)
    fats = models.FloatField(null=True)
    proteins = models.FloatField(null=True)
    carbs = models.FloatField(null = True)
    quantity = models.IntegerField(null=True, blank=True)
    total_calories = models.FloatField(null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.meal_of_the_day} - {self.total_calories} kcal"



=======
#Model for storing the mealtype.
class MealType(models.Model):
    MEALTYPE_CHOICES = [
    ('breakfast', 'breakfast'),
    ('lunch', 'lunch'),
    ('dinner', 'dinner')
    ]
    name = models. CharField(max_length=255,choices=MEALTYPE_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.name
    
#Model for storing the meal details.
class Meal(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='meals')
    mealtype= models.ForeignKey(MealType, on_delete=models.CASCADE, related_name='meals' )
    total_calories = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
#According to nutritional principles, carbs, and proteins contribute 4 calories per gram. 
# Fats contribute 9 calories per gram, Fiber 2 calories per gram.
    def total_calories(self):
        return self.nutritionalproduct.aggregate(total=Sum((Sum('carbohydrates')*4) + 
                                                           (Sum('proteins')*4) + (Sum('fiber')*2) + (Sum('fats')*9)))

    def __str__(self):
        return f"{self.user} - {self.mealtype} - {self.total_calories} intake on {self.date}"
     
#Model for storing the nutritional product details.
class NutritionalProduct(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='nutritionalproduct')
    name = models.CharField(max_length=255)
    carbohydrates = models.FloatField()
    proteins = models.FloatField()
    water = models.FloatField()
    fiber = models.FloatField()

    def __str__(self):
        return self.name



    


# Create your models here.
>>>>>>> 16526d6 (Project Setup, app creation, Models, and serializers creation)
