from djongo import models


class Users(models.Model):
    _id = models.ObjectIdField()
    UserId = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Number = models.CharField(max_length=10)


class Institutions(models.Model):
    _id = models.ObjectIdField()
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=10)
    # Users= models.ManyToOneRel(User)
