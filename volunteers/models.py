from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
       return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
       return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
       return self.name
class Availability(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
       return self.name

class Volunteer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE,null=True)
    def __str__(self):
       return self.name
    
