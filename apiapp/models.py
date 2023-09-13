from django.db import models

# Create your models here.


class Company(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    category=models.CharField(max_length=100,choices=
                              (('A','A'),
                               ('B','B'),
                               ('C','C')))
    created_at=models.DateField()
    active=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=200)
    designation=models.CharField(max_length=100)
    company_name=models.ForeignKey(Company,on_delete=models.CASCADE)
