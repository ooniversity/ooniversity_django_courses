# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from students.models import Student
from datetime import date

class StudentsTests(TestCase):
    
    def test_students(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, u'Иванов')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student1 = Student.objects.create(name='Ivan', surname=u'Иванов',
                    date_of_birth=date(1990, 10, 25), email='ivan@example.com',
                    phone='123', address='Earth', skype='ivanov')
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Иванов')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Иванов')
