from django.db import models

class evento(models.Model):
    ename = models.CharField(max_length = 100)
    edate = models.CharField(max_length=100)
    etime = models.CharField(max_length=100)
    eloc = models.CharField(max_length=100)
    enum = models.CharField(max_length=100)
    edisc = models.CharField(max_length=100)
    
class customer(models.Model):
    userid = models.CharField(max_length = 10)
    phoneno = models.CharField(max_length = 10)
    
class register(models.Model):
    username = models.CharField(max_length = 20)
    registeredevents = models.CharField(max_length = 50)
    