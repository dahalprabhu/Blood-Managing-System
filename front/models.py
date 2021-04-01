from django.db import models
from django.db.models import Model
# Create your models here.
class campaign(models.Model):
    camp_name= models.CharField(max_length=100)
    venue= models.CharField(max_length=100)
    time= models.DateTimeField()
    img=models.FileField(upload_to='pics')
    desc=models.TextField()

# Create your models here.
class bloodmanagement(models.Model):
 name=models.CharField(max_length=100)
 age1=models.IntegerField()
 blood_group=models.TextField()
 phone_no=models.CharField(max_length=15)
 address=models.CharField(max_length=100)


class cust(models.Model):
 name=models.CharField(max_length=100)
 age1=models.IntegerField()
 blood_group=models.TextField()
 phone_no=models.CharField(max_length=15)
 address=models.CharField(max_length=100)

 

class redcross_donater(models.Model):
 name=models.CharField(max_length=100)
 age1=models.IntegerField()
 blood_group=models.TextField()
 phone_no=models.CharField(max_length=15)
 address=models.CharField(max_length=100)



class hackersclub_donater(models.Model):
 name=models.CharField(max_length=100)
 age1=models.IntegerField()
 blood_group=models.TextField()
 phone_no=models.CharField(max_length=15)
 address=models.CharField(max_length=100)

 class ku_redcross(models.Model):
  name=models.CharField(max_length=100)
  age1=models.IntegerField()
  blood_group=models.TextField()
  phone_no=models.CharField(max_length=15)
  address=models.CharField(max_length=100)
