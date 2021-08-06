from django.db import models

class MangoFarm(models.Model):
    farm_name = models.CharField(max_length = 50)
    max_mangos = models.IntegerField()
    x_coord = models.FloatField()
    y_coord = models.FloatField()

class Customer(models.Model):
    customer_name = models.CharField(max_length = 50)
    mango_requirement = models.IntegerField()
    x_coord = models.FloatField()
    y_coord = models.FloatField()    
    city = models.CharField(max_length = 50)
    blacklisted = models.BooleanField(default=False);
