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
    subject = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    date = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField()

    ST_TODO = 'TODO'
    ST_DONE = 'DONE'
    ST_PAID = 'PAID'
    ST_RCVD = 'RCVD'

    STATUS_CHOICES = (
        (ST_TODO, 'To Do'),
        (ST_DONE, 'Done'),
        (ST_PAID, 'Paid'),
        (ST_RCVD, 'Received'),
    )

    POSSIBLE_STATUS = [s[0] for s in STATUS_CHOICES]

    status = models.CharField(
        max_length=4, choices=STATUS_CHOICES, default=ST_TODO)
