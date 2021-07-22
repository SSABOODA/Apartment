from django.db import models

class Public(models.Model):
    name             = models.CharField(max_length=50)
    password         = models.CharField(max_length=100)
    household_number = models.CharField(max_length=10, unique=True)
    payment          = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    
    class Meta:
        db_table = 'publics'




    
