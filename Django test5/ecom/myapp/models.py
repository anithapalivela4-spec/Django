from django.db import models

# Create your models here.

class product(models.Model):
    p_name = models.CharField(max_length=200)
    p_code = models.CharField(max_length=15)
    p_category = models.CharField(max_length=200)
    p_price = models.IntegerField()
    p_stock_quantity = models.IntegerField()
    p_description = models.TextField()
    p_avaiable_or_not = models.BooleanField(default=True)
    p_created_date = models.DateTimeField(auto_now_add=True)