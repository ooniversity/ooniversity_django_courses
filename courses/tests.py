from django.test import TestCase
from courses.models import Course, Lesson

class CourseTests(TestCase):
    
    def test_course_data(self):
        course1 = Course.objects.create(
                            name='Ruby',
                            short_description="Ruby is a dynamic, reflective, object-oriented, general-purpose programming language.")
        response = self.client.get('/')
        self.assertContains(response, "Ruby")

    def test_course_page(self):
        #from django.test import Client
        #client = Client()
        course1 = Course.objects.create(
                            name='Ruby',
                            short_description="Ruby is a dynamic, reflective, object-oriented, general-purpose programming language.")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_course_detail_page(self):
        course1 = Course.objects.create(
                            name='Ruby',
                            short_description="Ruby is a dynamic, reflective, object-oriented, general-purpose programming language.")
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)