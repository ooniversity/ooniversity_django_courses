from django.test import TestCase
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client


def create_course(name, short_description):
    return Course.objects.create(
                     name=name,
                     short_description=short_description)


class CourseTest(TestCase):

    def test_index_page_with_courses(self):
        client = Client()

        response = client.get('/index/')
        self.assertEqual(response.status_code, 200)

        course1 = create_course(
                     name='PyBursa02',
                     short_description="Wed development with Django")
        response = client.get('/index/')
        self.assertContains(response, "PyBursa02")


    def test_course_page(self):

        client = Client()

        response = client.get('/courses/1/')

        self.assertEqual(response.status_code, 404)

        course1 = create_course(
                         name='PyBursa02',
                         short_description="Wed development with Django")

        lesson1 = Lesson.objects.create(
                         topic='Introduction',
                         description='This is a first lesson',
                         course = course1,
                         index_numer = 1)

        lesson2 = Lesson.objects.create(
                         topic='Second lesscon',
                         description='This is a 2nd lesson',
                         course = course1,
                         index_numer = 2)

        response = client.get(reverse('courses:courses',
                                   args=(course1.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "PyBursa02")
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertContains(response, "This is a first lesson")
