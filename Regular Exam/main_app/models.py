from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):
        authors = self.get_queryset().all()
        # sorted_authors = sorted(authors, key=lambda x: (-x.article_set.count(), x.email))
        sorted_authors = authors.annotate(num_articles=models.Count('article')).order_by('-num_articles', 'email')
        return sorted_authors


class Author(models.Model):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(validators=[MaxValueValidator(2005), MinValueValidator(1900)])
    website = models.URLField(null=True, blank=True)
    objects = AuthorManager()


class Article(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    content = models.TextField(validators=[MinLengthValidator(10)])
    category = models.CharField(choices=(('Technology', 'Technology'), ('Science', 'Science'), ('Education', 'Education')), max_length=10, default='Technology')
    authors = models.ManyToManyField(to=Author)  # Allowing an article to have multiple authors and an author to have multiple articles
    published_on = models.DateTimeField(auto_now_add=True, editable=False)


class Review(models.Model):
    content = models.TextField(validators=[MinLengthValidator(10)])
    rating = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)  # Associating each review with an author
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)  # Associating each review with an article.
    published_on = models.DateTimeField(auto_now_add=True, editable=False)
