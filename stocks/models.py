from django.db import models

# Create your models here.

class Company(models.Model):
    ticker = models.CharField(max_length=10)
    co_name = models.CharField(max_length=50)
    latest_price = models.FloatField()
    previous_price =  models.FloatField()
    pe_ratio = models.FloatField()
    marketcap = models.FloatField()
    change = models.FloatField()

    def __str__(self):
        return self.ticker