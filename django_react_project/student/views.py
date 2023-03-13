from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from student.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    # If you want to limit access to logged in users
    # permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    # For complex queryset
    # def get_queryset(self):
    #     queryset = Student.objects.all()
    #     return queryset