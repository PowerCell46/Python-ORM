class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    page_count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
