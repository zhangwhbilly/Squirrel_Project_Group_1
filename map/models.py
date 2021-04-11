from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    uni_squirrel_id = models.CharField(
        help_text=_('Unique Squirrel Identification Number'),
        max_length = 255,
        primary_key = True,
    )

    latitude = models.FloatField(
        help_text=_('Latitude feature of the point'),
        blank = False,
    )

    longitude = models.FloatField(
        help_text=_('Longitude feature of the point'),
        blank = False,
    )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = [   
        (AM,_('AM')),
        (PM,_('PM')),
    ]

    shift = models.CharField(
        help_text=_('Shift'),
        choices=SHIFT_CHOICES,
        max_length = 255,
        blank = True,
    )
    
    date = models.DateField(
            help_text=_('Date'),
            null = True,
            blank = True,
        )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )
    
    age = models.CharField(
            help_text=_('Age is a choice between Adult and Juvenile'),
            max_length=50,
            choices=AGE_CHOICES,
            null = True,
            blank = True,
        )

    GRAY = 'Gray'
    BLACK = 'Black'
    CINNAMON = 'Cinnamon'

    COLOR_CHOICES = (
        (GRAY, 'Gray'),    
        (BLACK, 'Black'),
        (CINNAMON, 'Cinnamon'),
    )



    fur_color = models.CharField(
            help_text=_('Primary Fur Color'),
            max_length = 50,
            choices = COLOR_CHOICES,
            null = True,
            blank = True,
        )


    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'

    LOCATION_CHOICE= (
            (GROUND, 'Ground Plane'),
            (ABOVE, 'Above Ground'),
        )

    location = models.CharField(
            help_text=_('Location of the squirrels'),
            choices = LOCATION_CHOICE,
            max_length = 50,
            null = True,
            blank = True,
        )

    specific_location = models.CharField(
            help_text=_('Specific location of the squirrels'),
            max_length = 255,
            null = True,
            blank = True,
        )

    running = models.BooleanField(
            help_text=_('If the squirrel status is running'),
        )

    chasing = models.BooleanField(
            help_text=_('If the squirrel status is chasing'),
         )

    climbing = models.BooleanField(
            help_text=_('If the squirrel status is climbing'),
        )

    eating = models.BooleanField(
            help_text=_('If the squirrel status is eating'),
        )
     
    foraging = models.BooleanField(
            help_text=_('If the squirrel status is foraging'),
        )
     
    other_activities = models.CharField(
            help_text=_('Other activities'),
            max_length = 255,
            null = True,
            blank=True,
        )
            
    kuks = models.BooleanField(
            help_text=_('If the squirrel status was heard kuking'),
        )
        
    quaas = models.BooleanField(
            help_text=_('If the squirrel status was heard quaaing'),
        )
     
    moans = models.BooleanField(
            help_text=_('If the squirrel status was heard moaning'),
        )
            
    tail_flags = models.BooleanField(
            help_text=_('If the squirrel status was flaging its tail'),
        )
            
    tail_twitching = models.BooleanField(
            help_text=_('If the squirrel status was twitching its tail'),
        )
            
    approaches = models.BooleanField(
            help_text=_('If the squirrel status was approaching the observer'),
        )
            
    indifferent = models.BooleanField(
            help_text=_('If the squirrel status was indifferent to the observer'),
        )

    runs_from = models.BooleanField(
            help_text=_('If the squirrel status was running from the observer'),
        )    

    def __str__(self):
        return self.uni_squirrel_id
