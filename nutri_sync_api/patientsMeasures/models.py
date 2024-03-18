from django.db import models


class PatientsMeasures(models.Model):
    patientsId = models.BigIntegerField()
    nutriId = models.BigIntegerField()
    shoulder = models.DecimalField(max_digits=5, decimal_places=2)
    chest = models.DecimalField(max_digits=5, decimal_places=2)
    arm = models.DecimalField(max_digits=5, decimal_places=2)
    forearm = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    hip = models.DecimalField(max_digits=5, decimal_places=2)
    thigh = models.DecimalField(max_digits=5, decimal_places=2)
    calf = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'patients_measures'

    
    def save(self, *args, **kwargs):
        # if self.pk is not None:
        #     old_measure = PatientsMeasures.objects.get(pk=self.pk)
        #     PatientsMeasuresHist.objects.create(
        #         patientsId=old_measure.patientsId,
        #         shoulder=old_measure.shoulder,
        #         chest=old_measure.chest,
        #         arm=old_measure.arm,
        #         forearm=old_measure.forearm,
        #         waist=old_measure.waist,
        #         hip=old_measure.hip,
        #         thigh=old_measure.thigh,
        #         calf=old_measure.calf
        #     )

        super(PatientsMeasures, self).save(*args, **kwargs)