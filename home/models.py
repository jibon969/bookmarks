from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=120)
    roll = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


