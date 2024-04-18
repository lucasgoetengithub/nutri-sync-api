from django.db import models

class Folds(models.Model):
    patientsId = models.BigIntegerField()
    nutriId = models.BigIntegerField()
