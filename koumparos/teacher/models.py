from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(Teacher)
    subject = models.CharField(max_length=100)
    cost = models.FloatField()
    date = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField()
