from django.test import TestCase
from students.models import Student
from courses.models import Course

class StudentTests(TestCase):
    
    def test_student_all_data(self):
        course1 = Course.objects.create(
                            name='Ruby',
                            short_description="Ruby is a dynamic, reflective, object-oriented, general-purpose programming language.")
        student1 = Student.objects.create(
                            name='Paha',
                            surname="Tet",
                            email="paha@ukr.net",
                            birth_date='1978-03-12',
                            skype='vovan')
        response = self.client.get('/students/')
        self.assertContains(response, "Paha")
        student1.courses.add(course1)
        response = self.client.get('/students/?course_id=1')
        self.assertContains(response, "Paha")

    def test_student_all_page(self):
        student1 = Student.objects.create(
                            name='Paha',
                            surname="Tet",
                            email="paha@ukr.net",
                            birth_date='1978-03-12',
                            skype='vovan')
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_detail_data(self):
        student1 = Student.objects.create(
                            name='Paha',
                            surname="Tet",
                            email="paha@ukr.net",
                            birth_date='1978-03-12',
                            skype='vovan')
        response = self.client.get('/students/1/')
        self.assertContains(response, ".net")

    def test_student_detail_page(self):
    	#fixture = ['students']
        student1 = Student.objects.create(
                            name='Paha',
                            surname="Tet",
                            email="paha@ukr.net",
                            birth_date='1978-03-12',
                            skype='vovan')
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
