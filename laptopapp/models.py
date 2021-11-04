from django.db import models
from django.db.models.base import Model

class LaptopModel(models.Model):
    title = models.TextField()
    brand = models.CharField(max_length=255)
    ram_type = models.CharField(max_length=10)
    ram_capacity = models.IntegerField(default=0)
    ssd_present = models.BooleanField(default=False)
    ssd_capacity = models.CharField(default="0",max_length=255)
    hdd_present = models.BooleanField(default=False)
    hdd_capacity = models.CharField(default="0",max_length=255)
    size = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class PostImage(models.Model):
    laptop = models.ForeignKey(LaptopModel, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.laptop.title

class OrderModel(models.Model):
    choice = [
    ('IP', 'In Process'),
    ('OW', 'On the Way'),
    ('WC', 'With Customer'),
    ('C', 'Completed'),
    ('R', 'Rejected'),
]
    user_email = models.EmailField()
    laptop = models.ForeignKey(LaptopModel,on_delete=models.CASCADE)
    status = models.CharField(max_length=2,choices=choice,default="IP")
    start_date = models.CharField(max_length=20,default="0")
    end_date = models.CharField(max_length=20,default="0")
    total_price = models.CharField(max_length=255,default="0")

    def __str__(self) -> str:
        return str(self.user_email)+"=>"+str(self.status)
