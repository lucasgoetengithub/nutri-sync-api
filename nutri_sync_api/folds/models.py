from django.db import models

class Folds(models.Model):
    patientsId = models.BigIntegerField()
    nutriId = models.BigIntegerField()
    triceps = models.DecimalField(max_digits=5, decimal_places=2)
    subscapularis = models.DecimalField(max_digits=5, decimal_places=2)
    biceps = models.DecimalField(max_digits=5, decimal_places=2)
    axiliaryMedia = models.DecimalField(max_digits=5, decimal_places=2)
    thoracic = models.DecimalField(max_digits=5, decimal_places=2)
    supraIliac = models.DecimalField(max_digits=5,decimal_places=2)
    thigh = models.DecimalField(max_digits=5, decimal_places=2)
    medialCalf = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'folds'

    def save(self, *args, **kwargs):
        super(Folds, self).save(*args, **kwargs)