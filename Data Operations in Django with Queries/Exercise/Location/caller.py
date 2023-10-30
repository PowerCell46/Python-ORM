from main_app.models import Pet, Artifact, Location, Car, Task


def show_all_locations():
    locations = Location.objects.all().order_by('-id')
    return "\n".join(str(x) for x in locations)


def new_capital():
    new_capital = Location.objects.first()
    new_capital.is_capital = True
    new_capital.save()


def get_capitals():
    capitals = Location.objects.all().filter(is_capital=True).values('name')
    return capitals


def delete_first_location():
    Location.objects.first().delete()
