class WeatherForecast(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()
