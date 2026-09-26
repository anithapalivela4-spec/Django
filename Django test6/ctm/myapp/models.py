from django.db import models

# Create your models here.

class course(models.Model):
    c_name = models.CharField(max_length=200)
    c_duration = models.IntegerField()
    c_fees = models.IntegerField()
    c_trainer_name = models.CharField(max_length=200)
    c_mode_online_or_offline = models.CharField(max_length=200)
    c_start_date = models.DateField()
    c_number_of_seats = models.IntegerField()
    c_course_active_or_inactive = models.BooleanField(default=True)
