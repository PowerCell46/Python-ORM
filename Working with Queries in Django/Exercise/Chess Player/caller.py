def bulk_create_chess_players(*args) -> None:
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__lt=2400, rating__gte=2300).update(title='IM')


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__lt=2300, rating__gte=2200).update(title='FM')


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__lt=2200, rating__gte=0).update(title='regular player')
