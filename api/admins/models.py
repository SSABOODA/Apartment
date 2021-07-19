from django.db import models

class Admin(models.Model):
    name     = models.CharField(max_length=50)
    email    = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=100)
    payment  = models.ForeignKey('publics.Payment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'admins'
    

    
