from main_app.models import Pet, Artifact, Location, Car, Task

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    return f'The artifact {Artifact.objects.last().name} is {Artifact.objects.last().age} years old!'


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))

# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))
