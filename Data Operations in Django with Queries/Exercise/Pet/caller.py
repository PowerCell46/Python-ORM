from main_app.models import Pet, Artifact, Location, Car, Task


def create_pet(name: str, species: str):
    Pet.objects.create(name=name, species=species)
    return f'{Pet.objects.last().name} is a very cute {Pet.objects.last().species}!'

# # print(create_pet('Chakal', 'Dog'))
