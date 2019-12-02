from django.db import models
from django.utils.translation import gettext as _
import datetime as dt
import uuid

# Create your models here.
class Squirrel(models.Model):
    Latitude = models.DecimalField(
        help_text=_('Latitude'),
        default='',
        max_digits=19,decimal_places=15,)
    Longitude = models.DecimalField(
        help_text=_('Longitude'),
        default='',
        max_digits=19,decimal_places=15,)
    Unique_Squirrel_ID = models.CharField(
    	help_text=_('Unique_Squirrel_ID'),
        default='',
    	max_length=15)
    
    Date = models.DateField(
    	help_text=_('Date'),
        default='2000-01-01')

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'Unknown'
    AGE_CHOICES = (
        (ADULT, 'Adult'),(JUVENILE, 'Juvenile'),(UNKNOWN, 'Unknown'),
    )
    Age = models.CharField(
    	help_text=_('Age'),
        choices=AGE_CHOICES,
        default='Unknown',
        max_length = 50)
    Shift = models.CharField(
        help_text=_('Shift'),
        max_length=2)
    Primary_Fur_Color = models.CharField(
    	help_text=_('Primary_Fur_Color'),
        default='Unknown',
    	max_length = 50)
    Location = models.CharField(
    	help_text=_('Location1'),
    	max_length = 50)
    Specific_Location = models.CharField(
    	help_text=_('Specific_Location'),
    	max_length = 50)
    Other_Activities = models.CharField(
      help_text=_('Other_Activities'),
      max_length = 50)
    Running = models.BooleanField(
    	help_text=_('Running'),default=False,)
    Chasing = models.BooleanField(
    	help_text=_('Chasing'),default=False,)
    Climbing = models.BooleanField(
    	help_text=_('Climbing'),default=False,)
    Eating = models.BooleanField(
    	help_text=_('Eating'),default=False,)
    Foraging = models.BooleanField(
    	help_text=_('Foraging'),default=False,)
    Kuks = models.BooleanField(
    	help_text=_('Kuks'),default=False,)
    Quaas = models.BooleanField(
    	help_text=_('Quaas'),default=False,)
    Moans = models.BooleanField(
    	help_text=_('Moans'),default=False,)
    Tail_flags = models.BooleanField(
    	help_text=_('Tail_flags'),default=False,)
    Tail_twitches = models.BooleanField(
    	help_text=_('Tail_twitches'),default=False,)
    Approaches = models.BooleanField(
    	help_text=_('Approaches'),default=False,)
    Indifferent = models.BooleanField(
    	help_text=_('Indifferent'),default=False,)
    Runs_from = models.BooleanField(
    	help_text=_('Runs_from'),default=False,)


