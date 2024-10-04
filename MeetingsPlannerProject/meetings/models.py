from django.db import models

# Create your models here.
class meetings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
