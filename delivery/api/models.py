from django.db import models
from django.db.models.deletion import DO_NOTHING
from phone_field import PhoneField

# Create your models here.
class RestaurantList(models.Model):
    profile_picture = models.ImageField()
    name = models.CharField(max_length=30)
    address = models.TextField()
    owner_name = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=30)
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(null=True)
    opening_time = models.TimeField(null=True)
    closing_time = models.TimeField(null=True)
    rating = models.IntegerField(null=True)
    active = models.BooleanField(default=False)
    disable = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True,editable=False)
    updated_date = models.DateTimeField(auto_now=True,editable=True)
    # menu_list = models.TextField(default=None,null=True)

class MenuItems(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField()
    prep_time = models.IntegerField()
    is_veg = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True,editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=True)
    is_available = models.BooleanField()

gender_choices = (('M','Male'),('F','Female'),)
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


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    restaurant_id = models.ForeignKey(RestaurantList, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True,editable=False)
    updated_time = models.DateTimeField(auto_now=True, editable=True)
    total_amount = models.IntegerField()
    list_of_items = models.TextField(default=None,null=True)

class RestMenuItems(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField()
    prep_time = models.IntegerField()
    is_veg = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True,editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=True)
    is_available = models.BooleanField()
    restaurant = models.ForeignKey(RestaurantList, on_delete=models.DO_NOTHING)