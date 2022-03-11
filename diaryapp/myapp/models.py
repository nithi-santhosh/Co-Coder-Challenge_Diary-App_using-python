from django.db import models
from datetime import datetime
# Create your models here.
class Data(models.Model):
    time = models.DateTimeField(default=datetime.now, blank=True)
    heading = models.CharField(max_length=100, default='0')
    body = models.CharField(max_length=100, default='0')