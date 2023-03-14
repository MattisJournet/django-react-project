from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Student
from .serializers import StudentSerializer


class StudentTests(APITestCase):

    def setUp(self):
        self.student1 = Student.objects.create(
            last_name='Jack',
            first_name='Pierre'
        )
        self.student2 = Student.objects.create(
            last_name='Jack',
            first_name='Pierre'
        )

    def test_get_all_students(self):
        url = reverse('student-list')
        response = self.client.get(url)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        url = reverse('student-list')
        data = {
            'last_name': 'Jack',
            'first_name': 'Pierre'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 3)
        self.assertEqual(Student.objects.get(id=3).last_name, 'Jack')
        self.assertEqual(Student.objects.get(id=3).first_name, 'Pierre')

    def test_update_student(self):
        url = reverse('student-list')
        data = {
            'id': self.student1.id,
            'last_name': 'Jack',
            'first_name': 'Pierre'
        }
        response = self.client.put(url + f'{self.student1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.get(id=self.student1.id).last_name, 'Jack')
        self.assertEqual(Student.objects.get(id=self.student1.id).first_name, 'Pierre')

    def test_delete_student(self):
        url = reverse('student-list')
        response = self.client.delete(url + f'{self.student2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 1)
