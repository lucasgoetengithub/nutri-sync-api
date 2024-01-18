from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)

    class Meta:
        db_table = 'Users'