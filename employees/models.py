from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100,unique=True, blank=False)
    department = models.CharField(max_length=100, default='departament')

    def __str__(self) -> str:
        return self.name