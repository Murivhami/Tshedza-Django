from rest_framework import serializers
from .models import Meal, CustomUser

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['mealtype', 'total_calories', 'date']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'