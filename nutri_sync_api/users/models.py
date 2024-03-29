from django.db import models
from django.contrib.auth.hashers import make_password

class Users(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'Users'

    def save(self, *args, **kwargs):
        if self.pk is None or 'password' in kwargs:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)    