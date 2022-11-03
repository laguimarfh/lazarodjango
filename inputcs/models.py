from django.db import models

# import json
from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
# from django.contrib.auth import get_user_model
from django.urls import reverse

# User = get_user_model()

# Create your models here.


class Sheet(models.Model):
    """
    fields used to tracking defects on the CS process
    """
    PROCESS_CHOICES = [
        ('unknown', 'unknown'),
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4'),
        ('S5', 'S5'),
        ('S6', 'S6'),
        ('S7', 'S7'),
        ('S8', 'S8'),
        ('S9', 'S9'),
        ('S10', 'S10'),
        ('S11', 'S11'),
        ('S12', 'S12'),
        ('ED', 'ED'),
    ]
    DEFECT_CHOICES = [
        ('XS' , 'Excess'),
        ('WL' , 'Waterleak'),
        ('PH' , 'Pin Hole'),
        ('F' , 'Flick'),
        ('ED R' , 'ED run'),
        ('ED B' , 'ED Blister'),
        ('NS' , 'No Spat'),
        ('OF' , 'Off Location'),
        ('MC' , 'Missing Clip'),
        ('PA' , 'Poor Application'),
        ('NB' , 'No Brush'),
        ('G' , 'Gap'),
        ('MAS' , 'Mastic'),
        ('BB' , 'Body Bound'),
    ]
    SIDE_CHOICES = [
        ('LH' , 'Left Hand'),
        ('RH' , 'Right Hand'),
    ]
    LOCATION_CHOICES = [
        ('RR DOOR OUTTER' , 'Rear Door Outter'),
        ('RR DOOR INNER' , 'Rear Door Inner'),
        ('RR DOOR PERIMETER' , 'Rear Door Perimeter'),
        ('FR DOOR OUTTER' , 'Front Door Outter'),
        ('FT DOOR INNNER' , 'Front Door Inner'),
        ('FT DOOR PERIMETER' , 'Front Door Perimeter'),
        ('HOOD' , 'Hood'),
        ('HATCH' , 'Hatch'),
        ('HATCH PEREMETER' , 'Hatch Perimeter'),
        ('ROOF' , 'Roof'),
        ('FENDER' , 'Fender'),
        ('1/4 PANEL' , '1/4 Panel'),
        ('C PILAR' , 'C Pilar'),
        ('FUEL LID' , 'Fuel Lid'),
    ]
    process = models.CharField(max_length=30, choices=PROCESS_CHOICES, null=False)
    location = models.CharField(max_length=40, choices=LOCATION_CHOICES, null=False)
    defect = models.CharField(max_length=30, choices=DEFECT_CHOICES, null=False)
    side = models.CharField(max_length=30, choices=SIDE_CHOICES, null=False)
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    period = models.CharField(max_length=30, null=False, choices=[('1st', '1st'), ('2nd','2nd'), ('3rd','3rd'), ('4th','4th')])
    coorx = models.FloatField(null=False, blank=False, default=None)
    coory = models.FloatField(null=False, blank=False, default=None)
    photo = models.ImageField(blank=True, null=True,)
    
    class Meta:
        ordering = ['defect','-created']

    def get_absolute_url(self):
        return reverse('defect-detail', kwargs={"pk": self.pk})

