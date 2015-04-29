from django.test import TestCase
from django.test import Client

from courses.models import Course


class CoursesTests(TestCase):
    def test_pages(self):
        client = Client()

        response_courses = client.get('/courses/')

        self.assertEqual(response_courses.status_code, 200)

    def test_course_create(self):
        client = Client()

        course = Course.objects.create(
            name="Python",
            short_description='Some text.',
            description='Some long text.',
            )

        self.assertEqual(Course.objects.all().count(), 1)

        course_another = Course.objects.create(
            name="Django",
            short_description='Some text.',
            description='Some long text.',
            )

        self.assertEqual(Course.objects.all().count(), 2)

        response = client.get('/courses/')

        for item in Course.objects.all():
            self.assertContains(response, item)

    def test_course_detail(self):
        client = Client()

        course = Course.objects.create(
            name="Python",
            short_description='Some text.',
            description='Some long text.',
            )

        response = client.get('/courses/%s/' % Course.objects.get().pk)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course)