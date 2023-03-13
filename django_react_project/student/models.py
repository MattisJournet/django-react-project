from django.db import models



class Student(models.Model):
    last_name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"