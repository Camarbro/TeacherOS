from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    Id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 20)
    LastName = models.CharField(max_length = 20)
    Parent = models.OneToOneField(User)

    def __unicode__(self):
        return(self.Name + " " + self.LastName)

class Class(models.Model):
    Id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 20)
    Students = models.ManyToManyField(Student)

    def __unicode__(self):
        return "%s" %(self.Name)

class HomeWork(models.Model):
    Id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 20)
    Description = models.CharField(max_length = 75)
    Class = models.ForeignKey(Class, on_delete = models.CASCADE)
    DueDate = models.DateField()

    def __unicode__(self):
        return "%s" %(self.Name)

class Activities(models.Model):
    Id = models.AutoField(primary_key = True)
    Title = models.CharField(max_length = 30)
    Description = models.CharField(max_length = 30)
    Students = models.ForeignKey(Student)
    Done = models.BooleanField(default = False)

    def __unicode__(self):
        return "%s" %(self.Title)

class Reports(models.Model):
    Id = models.AutoField(primary_key = True)
    Subject = models.CharField(max_length = 30)
    Description = models.CharField(max_length = 30)
    Teacher = models.OneToOneField(User)
    Student = models.OneToOneField(Student)

    def __unicode__(self):
        return "%s" %(self.Subject)
