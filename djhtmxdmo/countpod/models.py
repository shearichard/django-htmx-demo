from django.db import models
from django.db import models


class CountLocation(models.Model):
    '''
    Represents an enclosed space access to which is limited by
    a number of, for instance, doors. 
    '''
    description_of_count_location = models.CharField(max_length=200)


class CountPoint(models.Model):
    '''
    Represents a point of access to a CountLocation, typically 
    a door.
    '''
    count_location = models.ForeignKey(CountLocation, on_delete=models.CASCADE)
    description_of_count_point = models.CharField(max_length=200)
    count = models.IntegerField(default=0)