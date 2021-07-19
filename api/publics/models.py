from django.db import models


class Public(models.Model):
    name             = models.CharField(max_length=50)
    email            = models.EmailField(max_length=45, unique=True)
    password         = models.CharField(max_length=100)
    household_number = models.CharField(max_length=10)
    payment          = models.ForeignKey('Payment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'publics'

class Payment(models.Model):
    payment = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)

    class Meta:
        db_table = 'payments'




    
