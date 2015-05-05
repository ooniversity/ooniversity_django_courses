
from django.test import TestCase, Client
from students.models import Student
from datetime import date


class StudentsTests(TestCase):

    def test_students(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, u'Zhulanov')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student1 = Student.objects.create(name='Sasha', surname=u'Zhulanov',
                                          date_of_birth=date(1991, 02, 26), email='sasha@nurekil.com',
                                          phone='3375544', address='Kharkov', skype='nurekil')
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Zhulanov')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Zhulanov')
