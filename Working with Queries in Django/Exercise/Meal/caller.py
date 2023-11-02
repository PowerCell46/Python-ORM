def set_new_chefs() -> None:
    Meal.objects.update(chef=Case(
  When(meal_type='Breakfast', then=Value('Gordon Ramsay')),
        When(meal_type='Lunch', then=Value('Julia Child')),
        When(meal_type='Dinner', then=Value('Jamie Oliver')),
        When(meal_type='Snack', then=Value('Thomas Keller'))
    ))


def set_new_preparation_times():
    Meal.objects.update(preparation_time=Case(
  When(meal_type='Breakfast', then=Value('10 minutes')),
        When(meal_type='Lunch', then=Value('12 minutes')),
        When(meal_type='Dinner', then=Value('15 minutes')),
        When(meal_type='Snack', then=Value('5 minutes'))
    ))


def update_low_calorie_meals() -> None:
    Meal.objects.filter(Q(meal_type='Breakfast') | Q(meal_type='Dinner')).update(calories=400)


def update_high_calorie_meals() -> None:
    Meal.objects.filter(Q(meal_type='Lunch') | Q(meal_type='Snack')).update(calories=700)


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(Q(meal_type='Lunch') | Q(meal_type='Snack')).delete()
