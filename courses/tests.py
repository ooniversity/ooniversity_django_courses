from django.test import TestCase
from courses.models import Course


class StudentTests(TestCase):

    def test_create_courses(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

        course_first = Course.objects.create(
            name="name_first",
            short_description="short_description_first",
            description="description_first",
        )
        self.assertEqual(Course.objects.all().count(), 1)

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name_first')

        course_second = Course.objects.create(
            name="name_second",
            short_description="short_description_second",
            description="description_second",
        )
        self.assertEqual(Course.objects.all().count(), 2)

        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name_second')
