class Location(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    population = models.PositiveIntegerField()
    description = models.TextField()
    is_capital = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} has a population of {self.population}!'
