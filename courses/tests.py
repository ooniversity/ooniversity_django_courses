from django.test import TestCase
from django.test import Client
from courses.models import Course

class CourseTest(TestCase):
    
    def test_list_courses(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    
    def test_course_create(self):
        client = Client()
        course1 = Course.objects.create(
            name = "Python",
            short_description = 'Best course',
            description = 'Python + Django = Bomba',
            )
        response = client.get('/')
        self.assertEqual(Course.objects.all().count(), 1)
        self.assertContains(response, "Python")
        
        # checking the detail info about course
        
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python')
        
