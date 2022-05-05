from django.db import models

# Create your models here.
class StaffDetailsModel(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email  = models.EmailField()
    department = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'staff_details'