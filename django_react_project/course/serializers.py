from rest_framework import serializers

from course.models import Course
from student.models import Student
from student.serializers import StudentSerializer


class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = '__all__'