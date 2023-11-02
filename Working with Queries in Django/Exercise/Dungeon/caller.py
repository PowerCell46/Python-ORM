def show_hard_dungeons() -> str:
    hard_dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')
    res = []
    for dungeon in hard_dungeons:
        res.append(f'{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!')
    return '\n'.join(res)


def bulk_create_dungeons(*args) -> None:
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names() -> None:
    Dungeon.objects.update(name=Case(
  When(difficulty='Easy', then=Value('The Erased Thombs')),
        When(difficulty='Medium', then=Value('The Coral Labyrinth')),
        When(difficulty='Hard', then=Value('The Lost Haunt'))
    ))


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)


def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.update(recommended_level=Case(
  When(difficulty='Easy', then=Value(25)),
        When(difficulty='Medium', then=Value(50)),
        When(difficulty='Hard', then=Value(75))
    ))


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(boss_health=500).update(reward='1000 Gold')
    Dungeon.objects.filter(location__startswith='E').update(reward='New dungeon unlocked')
    Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')


def set_new_locations() -> None:
    Dungeon.objects.update(location=Case(
  When(recommended_level=25, then=Value('Enchanted Maze')),
        When(recommended_level=50, then=Value('Grimstone Mines')),
        When(recommended_level=75, then=Value('Shadowed Abyss')),
    ))
