from django.db import models

# Create your models here.

class employee(models.Model):
    e_name = models.CharField(max_length=200)
    e_id = models.CharField(max_length=15)
    e_email = models.EmailField(max_length=200)
    e_department = models.CharField(max_length=200)
    e_job_role = models.CharField(max_length=200)
    e_salary = models.DecimalField(max_digits=10, decimal_places=2)
    e_date_of_joining = models.DateField()
    e_currently_working_or_not = models.BooleanField(default=True)
