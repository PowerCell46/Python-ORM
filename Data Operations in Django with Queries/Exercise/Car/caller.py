from main_app.models import Pet, Artifact, Location, Car, Task


def apply_discount():
    cars = Car.objects.all()
    for car in cars:
        years_str = str(car.year)
        years_sum = 0
        for char in years_str:
            years_sum += int(char)
        car.price_with_discount = car.price - ((car.price / 100) * years_sum)
        car.save()


def get_recent_cars():
    cars = Car.objects.all().filter(year__gte=2020).values('model', 'price_with_discount')
    return cars


def delete_last_car():
    Car.objects.last().delete()
