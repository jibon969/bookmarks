from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=120)
    roll = models.PositiveIntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


