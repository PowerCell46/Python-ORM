import os
import django
from django.db.models import Avg, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review


def get_authors(search_name=None, search_email=None):
    if not search_name and not search_email:
        return ""
    elif not search_name:
        authors = Author.objects.filter(email__icontains=search_email).order_by('-full_name')
    elif not search_email:
        authors = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')
    else:
        authors = Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email).order_by('-full_name')

    return '\n'.join([f'Author: {author.full_name}, email: {author.email}, status: {"Banned" if author.is_banned else "Not Banned"}' for author in authors])


def get_top_publisher() -> str:
    articles = Article.objects.all().count()
    if articles == 0:
        return ''

    authors = Author.objects.all()
    sorted_authors = sorted(authors, key=lambda x: (-x.article_set.count(), x.email))
    return f'Top Author: {sorted_authors[0].full_name} with {sorted_authors[0].article_set.count()} published articles.'


def get_top_reviewer():
    reviews = Review.objects.all().count()
    if reviews == 0:
        return ''

    authors = Author.objects.all()
    sorted_authors = sorted(authors, key=lambda x: (-x.review_set.count(), x.email))
    return f'Top Reviewer: {sorted_authors[0].full_name} with {sorted_authors[0].review_set.count()} published reviews.'


def get_latest_article():
    if Article.objects.count() == 0:
        return ''
    article = Article.objects.last()
    authors = article.authors.order_by('full_name').all()
    reviews = article.review_set.all()
    try:
        average = (sum(r.rating for r in reviews) / reviews.count())
    except:
        average = 0
    return f'The latest article is: {article.title}. Authors: {", ".join([a.full_name for a in authors])}. Reviewed: {reviews.count()} times. Average Rating: {average:.2f}.'


def get_top_rated_article():
    if Review.objects.count() == 1:
        return ""

    # top_article = Article.objects.annotate(
    #     num_reviews=Count('review'),
    #     avg_rating=Avg('review__rating')
    # ).order_by('-avg_rating', 'title').first()
    #
    # return f'The top-rated article is: {top_article.title}, with an average rating of {top_article.avg_rating:.2f}, reviewed {top_article.num_reviews} times.'

    articles = Article.objects.all()

    sorted_articles = sorted(articles, key=lambda x: (-(sum([r.rating for r in x.review_set.all()]) / x.review_set.count()), x.title))
    avg_rating = (sum([r.rating for r in sorted_articles[0].review_set.all()]) / sorted_articles[0].review_set.count())

    return(f'The top-rated article is: {sorted_articles[0].title}, with an average rating of {avg_rating:.2f}, reviewed {sorted_articles[0].review_set.count()} times.')


def ban_author(email=None):
    if Author.objects.count() == 0:
        return f'No authors banned.'
    elif email is None:
        return f'No authors banned.'

    try:
        banned_author = Author.objects.get(email=email)

    except:
        return f'No authors banned.'

    banned_author.is_banned = True
    banned_author.save()
    return_string = f'Author: {banned_author.full_name} is banned! {banned_author.review_set.all().count()} reviews deleted.'
    for review in banned_author.review_set.all():
        review.delete()
    return return_string

