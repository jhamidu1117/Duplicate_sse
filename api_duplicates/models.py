from django.db import models

# Create your models here.


class TRGid(models.Model):
    station_id = models.CharField(max_length=100)
    trg_id = models.CharField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200)

