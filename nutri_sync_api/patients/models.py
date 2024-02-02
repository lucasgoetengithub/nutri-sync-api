from django.db import models
from django.contrib.auth.hashers import make_password

class Patients(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.CharField(unique=True)
    password = models.CharField(max_length=128)
    age = models.IntegerField()
    dateOfBirth = models.DateField()
    address = models.CharField()
    occupation = models.CharField()
    obs = models.CharField()

    class Meta:
        db_table = 'Patients'
    
    def save(self, *args, **kwargs):
        if self.pk is None or 'password' in kwargs:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
