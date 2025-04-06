
# Tshedza-Django-Project

# **FitFair**


**Background**

Individuals are becoming more cautious about what they consume due to a lot of illnesses and diseases resulting from what people consume. The solution designed it to assist users to log meals on a daily basis to track how many calories they are taking and if they need to reduce.

**Features**

1. *Registration Page*: Allows user to register their profiles on the app.
2. *Log meal page*:Log meals together with calories for a specific day.
3. *Meal history*: A record of meals and calorie intake for the past days.

**Usage**

1. *SignUp and Login*: Create a new account if one is a new user and start logging and tracking meals.
2. *Log Meals*: Click on the Log Meal button to generate a new form to log daily meals.
3. *Track daily calories*: The meal_list provides a view of calorie intake per day.

**Technologies Used**
1. *Backend Language*: Python (3.13.1)
2. *Framework*: Django
3. *Styling*: HTML and CSS

**API Endpoints**

1. *Register a user* :http://127.0.0.1:8000/tracker/register/
   Method = POST
2. *Login*: http://127.0.0.1:8000/tracker/login/
   Method = POST
   A token is generated
4. *Log a meal* : POST http://127.0.0.1:8000/tracker/meals/
   Method = POST
   A token to log a meal.
6. *Retrieve meals for a user*: http://127.0.0.1:8000/tracker/meals/
   Method = GET.
7. *Update a meal*: http://127.0.0.1:8000/tracker/meals/{meal_id}/
   Method = PATCH OR PUT
8. *Delete a meal*: http://127.0.0.1:8000/tracker/meals/{meal_id}/
   Method = DELETE
   Retrieve the meal first then delete.
9. *Retrieve meal according to day and meal of the day*: http://127.0.0.1:8000/tracker/meals/?meal_of_the_day={meal_of_the_day}
    Method = GET


