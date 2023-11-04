class Song(models.Model):
    title = models.CharField(max_length=100, unique=True)
