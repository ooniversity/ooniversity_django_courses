from django.test import TestCase, Client
from courses.models import Course

class CoursesTests(TestCase):
    
    def test_courses(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'PyBursa-001')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(name='Test course PyBursa-001', 
                    short_description='Short descr', description='Full descr')
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PyBursa-001')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PyBursa-001')
