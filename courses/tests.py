from django.test import TestCase
from django.core.urlresolvers import reverse

from courses.models import Course, Lesson
from coaches.models import Coach


class CourseTests(TestCase):
    def test_course_list(self):
        from django.test import Client
        client = Client()

        course_1 = Course.objects.create(
            title='Css beginer',
            descr_sm='adhjka fshfkjd herwkehadns qeuijkandam',
        )
        course_1.save()

        course_2 = Course.objects.create(
            title='Art',
            descr_sm='dghadbkewrg sjathlkjenf iretkjnksnfgj lksjdflg',
        )
        course_2.save()

        response = client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.all().count(), 2)
        self.assertEqual(course_1.title, 'Css beginer')
        self.assertContains(response, u'fshfkjd')
        self.assertEqual(course_2.title, 'Art')
        self.assertContains(response, u'iretkjnksnfgj')

    def test_course_detail(self):
        from django.test import Client
        client = Client()

        course_1 = Course.objects.create(
            title='HTML',
            descr_sm='asdhjkasd adfjhkahsdn',
            descr_full='dsfkjf ajhfknsd sjhhjkjhwekru werhekjfdns wurhbdsfk',
            # coach = 'Asdjfk',
            # assistant = 'kdfjkds',
        )
        course_1.save()

        lesson_1 = Lesson.objects.create(
            theme='Tag head',
            descr='djkhsd ahjkhjhsd djkshsd',
            num_in_plan='1',
            course=course_1
        )
        lesson_1.save()

        response = client.get(reverse('courses:show', args=(course_1.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'HTML')
        self.assertContains(response, u'Tag head')
        self.assertEqual(lesson_1.num_in_plan, '1')
