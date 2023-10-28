class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
