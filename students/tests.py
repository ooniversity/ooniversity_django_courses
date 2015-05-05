# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from students.models import Student
from courses.models import Course

# Import functions creation courses and students
from testutils import create_course, create_student

# Import DATA objects (courses and students)
from data import get_course_1, get_course_2, get_course_3
from data import get_student_1, get_student_2


class StudentListViewTests(TestCase):

    def test_student_list_view_empty(self):

        response = self.client.get(reverse('students:student-list'))
        self.assertEqual(response.status_code, 200)		# Check load empty page

        # Check, when no registration students:
        self.assertContains(response, '< НЕТ зарегистрированных студентов >')
        self.assertQuerysetEqual(response.context['student_list'], [])


    def test_student_list_view_create(self):

        # Create courses for tests database
        course_1 = create_course(*get_course_1())
        course_2 = create_course(*get_course_2())
        course_3 = create_course(*get_course_3())

        # Create students for tests database
        # PARAMETRS: *(name, surname, date='%d-%m-%Y', email, skype, phone, addr), [<courses>]
        student_1 = create_student(*get_student_1(), courses=[course_1, course_2])
        student_2 = create_student(*get_student_2(), courses=[course_2])


        response = self.client.get(reverse('students:student-list'))

        # Check page with students:
        self.assertEqual(response.status_code, 200)			# Check load page
        self.assertEqual(Student.objects.all().count(), 2)	# Check counting students
        self.assertEqual(Course.objects.all().count(), 3)	# Check counting courses

        # Check data students on page:
        self.assertContains(response, u'Попов')				# Check student_1.surname
        self.assertContains(response, student_1.name)		# Check student_1.name
        self.assertContains(response, student_2.surname)	# Check student_2.surname
        self.assertContains(response, student_1.address)	# Check student_1.address
        self.assertContains(response, student_2.skype)		# Check student_2.skype
        # Check course_1 count on page
        self.assertContains(response, 'PY101', count=1)
        # Check course_2 count on page
        self.assertContains(response, course_2.title, count=2)
        # Check course_3 not page
        self.assertNotContains(response, 'JS')

        # Check buttons for students on page:
        self.assertContains(response, u'Добавить нового студента')	# button - Add student
        self.assertContains(response, u'Изменить', count=2*2)		# button - Change
        self.assertContains(response, u'Удалить', count=2*2)		# button - Delete



class StudentDetailViewTests(TestCase):

    def test_student_detail_view_unexist(self):
        pk = 1
        response = self.client.get(reverse('students:student-info', args=(pk,)))
        self.assertEqual(response.status_code, 404)			# Check unexist page


    def test_student_detail_view_create(self):

        # Create courses and student for tests database
        course_1 = create_course(*get_course_1())
        course_2 = create_course(*get_course_2())
        student_1 = create_student(*get_student_1(), courses=[course_1, course_2])

        # Create detail page about student
        response = self.client.get(reverse('students:student-info', args=(student_1.id,)))

        # Check page with student detail information:
        self.assertEqual(response.status_code, 200)			# Check load page
        self.assertEqual(Student.objects.all().count(), 1)	# Check counting students
        self.assertEqual(Course.objects.all().count(), 2)	# Check counting courses

        # Check student_1 (full_name) on page
        self.assertContains(response, u'{1} {0}'.format(student_1.name.upper(),
                                                        student_1.surname.upper()))
        # Check student_1.date_of_birth in format on page
        self.assertEqual(student_1.date_of_birth.strftime('%d-%m-%Y'), '15-09-1985')
        self.assertContains(response, u'15-сен-1985')		# Check student_1 (date_birth)

        # Check student_1 other field on page:
        self.assertContains(response, student_1.email)		# Check student_1.email
        self.assertContains(response, student_1.skype)		# Check student_1.skype
        self.assertContains(response, student_1.phone)		# Check student_1.phone
        self.assertContains(response, student_1.address)	# Check student_1.address

        # Check student_1.courses on page:
        self.assertContains(response, 'PY101')				# Check course_1
        self.assertContains(response, 'DJ101')				# Check course_2

