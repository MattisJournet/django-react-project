from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from course.models import Course
from course.serializers import CourseSerializer
from student.models import Student


class CourseViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class AddStudentToCours(views.APIView):
    def post(self, request, *args, **kwargs):
        # Extract the `student_id` and `course_id` values from the request data
        student_id = request.data.get('student_id', None)
        course_id = request.data.get('course_id', None)

        # Check if either the `student_id` or `course_id` values are missing from the request
        if not student_id or not course_id:
            # Return a 400 Bad Request response with an error message
            return Response('student_id or course_id missing', status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the `Course` and `Student` objects with the matching IDs
        course = get_object_or_404(Course, pk=course_id)
        student = get_object_or_404(Student, pk=student_id)

        # Add the `Student` object to the `students` ManyToManyField on the `Course` object
        course.students.add(student)
        # Save the updated `Course` object to the database
        course.save()

        # Return a 200 OK response to indicate that the operation was successful
        return Response(status=status.HTTP_200_OK)
