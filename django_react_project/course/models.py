from django.core.validators import MinValueValidator
from django.db import models
from student.models import Student


class Course(models.Model):
    course_name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    duration = models.FloatField(help_text="En heures", validators=[MinValueValidator(0)])
    students = models.ManyToManyField(to=Student, blank=True, default=None)

    def __str__(self):
        return f"{self.course_name} ({self.author})"