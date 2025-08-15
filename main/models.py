

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()

    def total(self):
        return self.subject1 + self.subject2 + self.subject3

    def average(self):
        return self.total() / 3

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A+'
        elif avg >= 75:
            return 'A'
        elif avg >= 60:
            return 'B'
        elif avg >= 40:
            return 'C'
        else:
            return 'F'

    def __str__(self):
        return self.name

