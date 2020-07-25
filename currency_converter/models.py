from django.db import models
class Currency(models.Model):
    country_name = models.CharField(max_length=50)
    currency_symbol = models.CharField(max_length=50)
    currency_name = models.CharField(max_length=50)
    currency_id = models.CharField(max_length=50)

    def __str__(self):
        return self.currency_name
