from django.db import models

class Bioimpedance(models.Model):
    nutriId = models.BigIntegerField()
    patientId = models.BigIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    bodyFat = models.DecimalField(max_digits=5, decimal_places=2)
    muscleRate = models.DecimalField(max_digits=5, decimal_places=2)
    fatFreeDough = models.DecimalField(max_digits=5, decimal_places=2)
    subcutaneosFat = models.DecimalField(max_digits=5, decimal_places=2)
    visceralFat = models.DecimalField(max_digits=5, decimal_places=2)
    bodyWater = models.DecimalField(max_digits=5, decimal_places=2)
    skeletalMuscleMass = models.DecimalField(max_digits=5, decimal_places=2)
    muscleMass = models.DecimalField(max_digits=5, decimal_places=2)
    boneMass = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)    
    muscleMass = models.DecimalField(max_digits=5, decimal_places=2)
    basalMetabolicRate = models.DecimalField(max_digits=50, decimal_places=2)


    class Meta:
        db_table = 'bioimpedance'