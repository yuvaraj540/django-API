from django.db import models

class app(models.Model):
    id = models.IntegerField(primary_key=True)
    cus_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    # Create your models here.
    