from django.db import models

class Bioimpedance(models.Model):
    nutriId = models.BigIntegerField()
    patientId = models.BigIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    bodyFat = models.DecimalField(max_digits=5, decimal_places=2)
    muscleRate = models.DecimalField(max_digits=5, decimal_places=2)
    fatFreeDough = models.DecimalField(max_digits=5, decimal_places=2)
