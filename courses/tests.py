# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from courses.models import Course, Lesson
from coaches.models import Coach

# Import functions creation courses and lessons
from testutils import create_course, create_lesson

# Import DATA objects (courses and lessons)
from data import get_course_1, get_course_2, get_course_3, get_course_4
from data import get_lesson_1, get_lesson_2, get_lesson_3


class IndexCourseListTests(TestCase):

    def test_index_course_list_empty(self):

        response = self.client.get(reverse('index-ooniversity'))
        self.assertEqual(response.status_code, 200)			# Check load empty page

        # Check, when no courses in database:
        self.assertContains(response, '< Список курсов - ПУСТ >')
        self.assertQuerysetEqual(response.context['courses'], [])


    def test_index_course_list_create(self):

        # Create courses for tests database
        course_1 = create_course(*get_course_1())
        course_2 = create_course(*get_course_2())
        course_3 = create_course(*get_course_3())
        course_4 = create_course(*get_course_4())

        response = self.client.get(reverse('index-ooniversity'))

        # Check page with courses:
        self.assertEqual(response.status_code, 200)			# Check load page
        self.assertEqual(Course.objects.all().count(), 4)	# Check counting courses

        # Check data courses on page:
        self.assertContains(response, course_1.title)		# Check course_1.title
        self.assertContains(response, 'RUBI')				# Check course_4.title
        # Check course_2.short_descript on page
        self.assertContains(response, course_2.short_descript)
        # Check course_3.short_descript on page
        self.assertContains(response, u'JavaScript')

        # Check buttons for courses on page:
        self.assertContains(response, u'Добавить новый курс')	# button - Add course
        self.assertContains(response, u'Изменить', count=4*2)	# button - Change
        self.assertContains(response, u'Удалить', count=4*2)	# button - Delete



class CourseDetailViewTests(TestCase):

    def test_course_detail_view_unexist(self):
        pk = 1
        response = self.client.get(reverse('courses:course-coaches', args=(pk,)))
        self.assertEqual(response.status_code, 404)			# Check unexist page


    def test_course_detail_view_create(self):

        # Create course, coaches and lessons for tests database
        course_1 = create_course(*get_course_1())
        lesson_1 = create_lesson(*get_lesson_1(), course=course_1)
        lesson_2 = create_lesson(*get_lesson_2(), course=course_1)
        lesson_3 = create_lesson(*get_lesson_3(), course=course_1)

        # Create detail page about course	# with lessons
        response = self.client.get(reverse('courses:course-coaches', args=(course_1.id,)))

        # Check page with course detail information:
        self.assertEqual(response.status_code, 200)			# Check load page
        self.assertEqual(Course.objects.all().count(), 1)	# Check counting courses
        self.assertEqual(Lesson.objects.all().count(), 3)	# Check counting lessons
        # Check counting lessons in course_1
        self.assertEqual(course_1.lesson_set.all().count(), 3)

        # Check course_1 (title and description) show on page
        self.assertContains(response, course_1.title, count=3)
        self.assertContains(response, course_1.description)

        # Check show lessons on page about course:
        self.assertContains(response, u'Основы Python')		# Check lesson_1.theme
        self.assertContains(response, lesson_2.description)	# Check lesson_2.description
        self.assertContains(response, lesson_3.number)		# Check lesson_3.number

        # Check button for add lesson on page:
        self.assertContains(response, u'Добавить занятие')	# button - Add lesson

