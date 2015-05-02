from django.test import TestCase
from courses.models import Course
from students.models import Student
from courses.tests import create_course
from django.core.urlresolvers import reverse
from django.test import Client


class StudentTest(TestCase):

    def test_page_with_all_students(self):
        client = Client()

        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

        course1 = create_course(
                     name='PyBursa02',
                     short_description="Wed development with Django")

        student = Student.objects.create(
                      name = 'Peter',
                      surname = 'Petrov',
                      date_of_birth = '1990-03-27',
                      email = 'petr@gmail.com',
                      phone = '+380507892546',
                      address = 'ul. Petrovskogo',
                      skype = 'petro')
        student.courses.add(course1)
        response = client.get('/students/')
        self.assertContains(response, "ul. Petrovskogo")

    def test_student_page(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

        course1 = create_course(
                     name='PyBursa02',
                     short_description="Wed development with Django")

        student = Student.objects.create(
                      name = 'Peter',
                      surname = 'Petrov',
                      date_of_birth = '1990-03-27',
                      email = 'petr@gmail.com',
                      phone = '+380507892546',
                      address = 'ul. Petrovskogo',
                      skype = 'petro')
        student.courses.add(course1)
        response = client.get(reverse('students:student_d',
                                   args=(course1.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Peter")
