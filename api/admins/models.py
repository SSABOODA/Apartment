from django.db import models

class Admin(models.Model):
    name     = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'admins'
    

    
