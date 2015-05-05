from django.test import TestCase, Client
from courses.models import Course

class CoursesTests(TestCase):

    def test_courses(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        test1 = Course.objects.create(name='Testcourse1', short_description='Short', description='Full')
        self.assertEqual(Course.objects.all().count(), 1)
        response = c.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Testcourse1')
        test2 = Course.objects.create(name='Testcourse2', short_description='Short', description='Full')
        self.assertEqual(Course.objects.all().count(), 2)
        response = c.get('/courses/2/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Testcourse2')