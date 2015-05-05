from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from courses.models import Course, Lesson


class CourseTest(TestCase):

    def test_course_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No courses here')

        course1 = Course.objects.create(name='Eng 101', brief='English 101')
        course2 = Course.objects.create(name='Eng 102', brief='English 102')
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.all().count(), 2)

        for contextData in Course.objects.all():
            self.assertContains(response, contextData.name)
            self.assertContains(response, contextData.description)


class CourseDetailTest(TestCase):

    def test_course_detail(self):
        courseNumber = 1
        client = Client()
        response = client.get(reverse('courses:course', args=(courseNumber,)))
        self.assertEqual(response.status_code, 404)

        nCourse = Course.objects.create(name='Eng 101', brief='English 101',
                                        description=u'Learn english!')

        for i in xrange(10):
            nLesson = Lesson.objects.create(theme=u'Theme # {}'.format(i),
                                               description='Desc # {}'.format(i),
                                               course=nCourse,
                                               number=i,)

        response = client.get(reverse('courses:course', args=(courseNumber,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, nCourse.name.upper())

        for lesson in nCourse.lesson_set.all():
            self.assertContains(response, lesson.theme)



