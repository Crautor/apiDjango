from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    departament = models.CharField(max_length=100)

    def __str__(self):
        return f'Name:{self.name} - Email:{self.email} - Departament:{self.departament}'