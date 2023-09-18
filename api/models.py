from django.db import models


# Create your models here.
class Company(models.Model):
    
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()


class Club(models.Model):
    """
    Model principal.
    """

    name = models.CharField(max_length=100)
    club_colors = models.CharField(max_length=100)
    year_foundation = models.PositiveIntegerField()
    stadium = models.CharField(max_length=150)
