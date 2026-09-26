from django.db import models

# Create your models here.

class student(models.Model):
    s_name = models.CharField(max_length=200)
    s_phone = models.CharField()
    s_email = models.CharField()
    s_marks = models.IntegerField()

class faculty(models.Model):
    f_name = models.CharField(max_length=200)
    f_phone = models.CharField()
    f_email = models.CharField()
    f_salary = models.IntegerField()

class course(models.Model):
    c_name = models.CharField(max_length=200)
    c_duration = models.IntegerField()
    c_fees = models.IntegerField()

class department(models.Model):
    d_name = models.CharField(max_length=200)
    d_head = models.CharField(max_length=200)
    d_location = models.CharField(max_length=200)
