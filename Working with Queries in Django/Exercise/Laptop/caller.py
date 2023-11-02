def show_the_most_expensive_laptop() -> str:
    most_expensive = Laptop.objects.order_by('-price', ' id').first()
    return f'{most_expensive.brand} is the most expensive laptop available for {most_expensive.price}$!'


def bulk_create_laptops(*args) -> None:
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(Q(brand='Asus') | Q(brand='Lenovo')).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(Q(brand='Apple') | Q(brand='Dell') | Q(brand='Acer')).update(memory=16)


def update_operation_systems() -> None:
    Laptop.objects.update(
        operation_system=Case(
  When(brand='Asus', then=Value('Windows')),
        When(brand='Apple', then=Value('MacOS')),
        When(brand__in=['Dell', 'Acer'], then=Value('Linux')),
        When(brand='Lenovo', then=Value('Chrome OS')),
        default=F('operation_system'))
    )


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()
