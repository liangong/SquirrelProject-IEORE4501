from django.db import models


# Create your models here.

class SquirrelData(models.Model):
    SHIFT_CHOICE = (('AM', 'AM'), ('PM', 'PM'))
    latitude = models.FloatField(verbose_name='latitude')
    longitude = models.FloatField(verbose_name='longitude')
    unique_squirrel_id = models.CharField(verbose_name='unique squirrel id', max_length=30, unique=True)
    shift = models.CharField(max_length=2, choices=SHIFT_CHOICE)
    date = models.DateField()
    age = models.CharField(max_length=15, null=True, blank=True)
    primary_fur_color = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    specific_location = models.CharField(max_length=100, null=True, blank=True)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length=200, blank=True, null=True)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()

    class Meta:
        db_table = 'squirrel_data'

    def __str__(self):
        return self.unique_squirrel_id


