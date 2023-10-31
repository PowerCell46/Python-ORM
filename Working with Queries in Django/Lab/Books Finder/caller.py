def find_books_by_genre_and_language(book_genre: str, book_language: str):
    return Book.objects.all().filter(genre=book_genre, language=book_language)
