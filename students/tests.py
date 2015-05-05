from django.test import TestCase, Client
from students.models import Student
from datetime import date

class StudentsTests(TestCase):
    
    def test_students(self):
        c = Client()
        response = c.get('/students/')
        self.assertEqual(response.status_code, 200)
        test1 = Student.objects.create(name='Ivan', surname='Ivanov',
                                        date_of_birth=date(1984, 02, 16), email='ivan@testing.com',
                                        phone='+380000', address='example address', skype='ivan')
        response = c.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 1)
        self.assertContains(response, 'Ivanov')
        test2 = Student.objects.create(name='Petr', surname='Petrov',
                                        date_of_birth=date(1984, 02, 16), email='petrov@testing.com',
                                        phone='+380000', address='example address', skype='petr')
        response = c.get('/students/2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 2)
        self.assertContains(response, 'Petrov')