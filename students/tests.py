from django.test import TestCase
from datetime import datetime
from students.models import Student
from courses.models import Course


class StudentTests(TestCase):

    def test_create_student(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

        student_first = Student.objects.create(
            name="name_first",
            surname="surname_first",
            date_of_birth=datetime.now().date(),
            email="email_first@gmail.com",
            phone="+380509602555",
            address="address_first",
            skype="skype_first",
        )
        course_first = Course.objects.create(
            name="name_first",
            short_description="short_description_first",
            description="description_first",
        )
        student_first.course.add(course_first)
        self.assertEqual(Student.objects.all().count(), 1)

        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name_first')

        student_second = Student.objects.create(
            name="student_second",
            surname="surname_second",
            date_of_birth=datetime.now().date(),
            email="email_second@gmail.com",
            phone="+380509602555",
            address="address_second",
            skype="skype_second",
        )

        # student_second.course.add(course_first)
        self.assertEqual(Student.objects.all().count(), 2)

        response = client.get('/students/2/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "email_second@gmail.com")

