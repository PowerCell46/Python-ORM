def show_highest_rated_art() -> str:
    best_art = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f'{best_art.art_name} is the highest-rated art with a {best_art.rating} rating!'


def bulk_create_arts(first_art, second_art) -> None:
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()
