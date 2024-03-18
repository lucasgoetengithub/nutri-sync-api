from django.db import models
from django.contrib.auth.hashers import make_password

class Patients(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    gender = models.CharField()
    email = models.CharField(unique=True)
    password = models.CharField(max_length=128)
    dateOfBirth = models.DateField()
    address = models.CharField()
    city = models.CharField()
    occupation = models.CharField()
    obs = models.CharField()
    phoneContact = models.CharField()
    nutriID = models.BigIntegerField()
    

    class Meta:
        db_table = 'Patients'
    
    def save(self, *args, **kwargs):
        if self.pk is None or 'password' in kwargs:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
