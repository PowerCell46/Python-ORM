class Laptop(models.Model):
    BRAND_CHOICES = (('Asus', 'Asus'), ('Acer', 'Acer'), ('Apple', 'Apple'), ('Lenovo', 'Lenovo'), ('Dell', 'Dell'))
    OPERATION_SYSTEM_CHOICES = (('Windows', 'Windows'), ('MacOS', 'MacOS'), ('Linux', 'Linux'), ('Chrome OS', 'Chrome OS'))
    brand = models.CharField(choices=BRAND_CHOICES, max_length=100)
    processor = models.CharField(max_length=100)
    memory = models.PositiveIntegerField(help_text='Memory in GB')
    storage = models.PositiveIntegerField(help_text='Storage in GB')
    operation_system = models.CharField(choices=OPERATION_SYSTEM_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
