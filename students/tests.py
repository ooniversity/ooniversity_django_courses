import datetime

from django.test import TestCase
from django.test import Client

from students.models import Student


class StudentsTests(TestCase):
    def test_pages(self):
        client = Client()
        
        response_students = client.get('/students/')

        self.assertEqual(response_students.status_code, 200)

    def test_student_create(self):
        client = Client()

        student = Student.objects.create(
            name='Name',
            surname='Surname',
            date_of_birth=datetime.date.today(),
            email='example@example.com',
            phone='+380501234567',
            skype='skype',
            )

        self.assertEqual(Student.objects.all().count(), 1)

        student_another = Student.objects.create(
            name='Vasya',
            surname='Pupkin',
            date_of_birth=datetime.date.today(),
            email='another@example.com',
            phone='+380507654321',
            skype='another',
            )

        self.assertEqual(Student.objects.all().count(), 2)

        response = client.get('/students/')

        for item in Student.objects.all():
            self.assertContains(response, item)

    def test_student_detail(self):
        client = Client()

        student = Student.objects.create(
            name='Vasya',
            surname='Pupkin',
            date_of_birth=datetime.date.today(),
            email='example@example.com',
            phone='+380501234567',
            skype='skype',
            )

        response = client.get('/students/%s/' % Student.objects.get().pk)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, student)