from django.db import models
from datetime import datetime

class Jobs(models.Model):
    title = models.CharField(max_length = 15)
    work_class = models.CharField(max_length = 20)
    place = models.CharField(max_length = 20)
    work_time = models.CharField(max_length = 20)
    salary = models.CharField(max_length = 20)
    text = models.CharField(max_length = 250)
    created_date = models.DateField()

    class Meta():
        db_table = 'jobs'