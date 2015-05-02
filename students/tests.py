from django.test import TestCase
from django.test import Client
from students.models import Student
from datetime import date

class StudentTest(TestCase):
 
    def test_list_students(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)


    def test_student_create(self):
        client = Client()
        student1 = Student.objects.create(
            name = "Nickolas",
            surname = 'Popandopolas	',
            date_of_birth = date(1989, 12, 19),
            email = 'np@gmail.com',
            phone = '123456789',
            address = 'address',
            skype = 'np',
            )
        response = client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 1)
        self.assertContains(response, "Nickolas")

        # checking the detail info about student
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Popandopolas')
        
