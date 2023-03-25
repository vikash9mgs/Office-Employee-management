from django.db import models


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.CharField(default=0, max_length=100)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.CharField(default=0, max_length=100)
    phone = models.IntegerField(default=0)
    address = models.CharField(default=0, max_length=100)
    location = models.CharField(default=0, max_length=100)
    email = models.EmailField(default=0, max_length=50)
    hire_date = models.DateField()
    photo = models.FileField(upload_to="photo/", max_length=250, null=True, default=None)


class adminInfo(models.Model):
    email = models.EmailField(default=0, max_length=50)
    psd = models.CharField(max_length=100, null=False)
