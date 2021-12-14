from django.db import models
from phone_field import PhoneField

gender_choices = (('M','Male'),('F','Female'))

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    profile_picture = models.ImageField()
    dob = models.DateTimeField()
    mobile = PhoneField()
    address = models.TextField()
    gender = models.CharField(max_length=1,choices=gender_choices,default='M')
    nationality = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True,editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=True)
