from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Student, Course


from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Course
from django.db import connection


class DatabaseConnectionTestCase(TestCase):
    def test_database_connection(self):
        # Try to access the database by executing a simple query
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

        # Check that the query returned the expected result
        self.assertEqual(result, (1,))


class CourseViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(
            course_name='Test Course',
            author='Test Author',
            duration=1.5,
        )

    def test_list_courses(self):
        url = reverse('course-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['course_name'], self.course.course_name)

    def test_create_course(self):
        url = reverse('course-list')
        data = {
            'course_name': 'New Course',
            'author': 'New Author',
            'duration': 2.0,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)
        self.assertEqual(Course.objects.last().course_name, 'New Course')

    def test_retrieve_course(self):
        url = reverse('course-detail', args=[self.course.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['course_name'], self.course.course_name)

    def test_update_course(self):
        url = reverse('course-detail', args=[self.course.pk])
        data = {
            'course_name': 'Updated Course',
            'author': 'Updated Author',
            'duration': 2.5,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.course.refresh_from_db()
        self.assertEqual(self.course.course_name, 'Updated Course')
        self.assertEqual(self.course.author, 'Updated Author')
        self.assertEqual(self.course.duration, 2.5)

    def test_delete_course(self):
        url = reverse('course-detail', args=[self.course.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)


class AddStudentToCoursTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.student1 = Student.objects.create(first_name='Pierre', last_name='Jack')
        self.student2 = Student.objects.create(first_name='Henri', last_name='Jack')
        self.course1 = Course.objects.create(course_name='English 101', author='John Smith', duration=2.5)
        self.course2 = Course.objects.create(course_name='Math 101', author='Jane Doe', duration=3.0)

    def test_add_student_to_course_success(self):
        # Define the request data
        data = {'student_id': self.student1.id, 'course_id': self.course1.id}

        # Issue a POST request to the view with the request data
        url = reverse('add-student-to-course')
        response = self.client.post(url, data, format='json')

        # Check that the response has a status code of 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the student was added to the course
        self.assertIn(self.student1, self.course1.students.all())

    def test_add_student_to_course_missing_fields(self):
        # Define the request data with a missing student_id field
        data = {'course_id': self.course1.id}

        # Issue a POST request to the view with the request data
        url = reverse('add-student-to-course')
        response = self.client.post(url, data, format='json')

        # Check that the response has a status code of 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Define the request data with a missing course_id field
        data = {'student_id': self.student1.id}

        # Issue a POST request to the view with the request data
        response = self.client.post(url, data, format='json')

        # Check that the response has a status code of 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_student_to_course_invalid_student_id(self):
        # Define the request data with an invalid student_id value
        data = {'student_id': 9999, 'course_id': self.course1.id}

        # Issue a POST request to the view with the request data
        url = reverse('add-student-to-course')
        response = self.client.post(url, data, format='json')

        # Check that the response has a status code of 404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_student_to_course_invalid_course_id(self):
        # Define the request data with an invalid student_id value
        data = {'student_id': self.student1.id, 'course_id': 9999}

        # Issue a POST request to the view with the request data
        url = reverse('add-student-to-course')
        response = self.client.post(url, data, format='json')

        # Check that the response has a status code of 404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)