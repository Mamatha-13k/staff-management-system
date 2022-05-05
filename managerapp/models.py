from django.db import models

# Create your models here.
class ManagerDetailsModel(models.Model):
    manager_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email  = models.EmailField()
    department = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default='pending')

    class Meta:
        db_table = 'manager_details'
