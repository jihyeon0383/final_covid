from django.db import models

class Covid(models.Model):
    date = models.CharField(max_length=8, blank=True)
    country = models.CharField(max_length=100, blank=True)
    confirmed = models.FloatField(null=True)
    recovered = models.FloatField(null=True)
    deaths = models.FloatField(null=True)

    def __str__(self):
        return self.country