from datetime import datetime
from django.db import models
from django.db.models.fields import TimeField

# Create your models here.


class ongoingridesnow(models.Model):
    bikenum = models.TextField()
    ridername = models.CharField(max_length=150)
    ridernum = models.TextField()
    date_time = models.DateTimeField()
    currentlocation = models.TextField()


class alertsandnote(models.Model):
    info_alert = models.TextField()
    dateandtime = models.DateTimeField()


class logos(models.Model):
    logo = models.ImageField(upload_to='pics')
    bikelogo = models.ImageField(upload_to='imgs')


class allorderslist(models.Model):
    order_num = models.TextField()
    date_of_order = models.DateTimeField()
    bike_num = models.TextField()
    rider_name = models.CharField(max_length=150)
    id_proof = models.TextField()
    total_kms = models.IntegerField()
    total_time = models.IntegerField()
    amount = models.IntegerField()
    payment = models.TextField()
    bike_collector = models.TextField()
    booking_charges = models.IntegerField()
