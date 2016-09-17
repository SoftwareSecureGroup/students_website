from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Student(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

    student_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    grade = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='upload', null=True)
    password = models.CharField(max_length=64)


class Admin(models.Model):
    admin_id = models.CharField(max_length=10)
    password = models.CharField(max_length=64, null=True)
