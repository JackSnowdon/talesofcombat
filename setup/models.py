from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Race(models.Model):
    race_name = models.CharField(max_length=100)
    buffs = models.IntegerField()
    saps = models.IntegerField()

    def __str__(self):
        return self.race_name

class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    max_hp = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    max_mp = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)])
    power = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    defence = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    social = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    magik = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    wisdom = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    dex = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    soul = models.IntegerField()
    
    def __str__(self):
        return self.name

