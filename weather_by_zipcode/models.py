from django.db import models
from datetime import datetime
from django.utils import timezone

class Zipcode(models.Model):
    your_zipcode = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)
    temp = models.FloatField(default=0)
    feels_like = models.FloatField(default=0)
    temp_max = models.FloatField(default=0)
    pressure = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.your_zipcode)
    
    def was_queried_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
