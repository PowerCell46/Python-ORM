def show_workouts() -> str:
    res = []
    selected = Workout.objects.filter(Q(workout_type='Calisthenics') | Q(workout_type='CrossFit'))
    for s in selected:
        res.append(f'{s.name} from {s.workout_type} type has {s.difficulty} difficulty!')

    return '\n'.join(res)


def get_high_difficulty_cardio_workouts() -> None:
    return Workout.objects.filter(workout_type='Cardio').filter(difficulty='High').order_by('instructor')


def set_new_instructors() -> None:
    Workout.objects.update(instructor=Case(
        When(workout_type='Cardio', then=Value('John Smith')),
        When(workout_type='Strength', then=Value('Michael Williams')),
        When(workout_type='Yoga', then=Value('Emily Johnson')),
        When(workout_type='CrossFit', then=Value('Sarah Davis')),
        When(workout_type='Calisthenics', then=Value('Chris Heria')),
    ))


def set_new_duration_times() -> None:
    Workout.objects.update(duration=Case(
        When(instructor='John Smith', then=Value('15 minutes')),
        When(instructor='Sarah Davis', then=Value('30 minutes')),
        When(instructor='Chris Heria', then=Value('45 minutes')),
        When(instructor='Michael Williams', then=Value('1 hour')),
        When(instructor='Emily Johnson', then=Value('1 hour and 30 minutes')),
    ))


def delete_workouts() -> None:
    Workout.objects.exclude(Q(workout_type='Strength') | Q(workout_type='Calisthenics')).delete()
