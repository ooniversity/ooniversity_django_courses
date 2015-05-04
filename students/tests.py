# -*- coding: utf_8 -*-
import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from students.models import Students
from courses.models import Courses


def add_course(student, course):
    for item in course:
        cou = Courses.objects.create(name='Курс %s' % item, description='Описание курса по %s' % item)
        student.course.add(cou)
    return student


def create_student(name, surname, course):
    student = Students.objects.create(first_name=name,
                                      surname=surname,
                                      birdth_date=datetime.date(1986, 3, 25),
                                      adress='Киев, ул. Артема, 56, кв 11',
                                      email='sergei.4e@gmail.com',
                                      skype='sergei.4e',
                                      phone='0446782453')
    add_course(student, course)
    return student


class StudentsViewTests(TestCase):

    def test_students_view_with_no_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Пока-что нет ни одного студента")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_students_view_with_one_student(self):
        create_student(name='Валера', surname='Пономаренко', course=['Python'])
        response = self.client.get('/students/')
        self.assertQuerysetEqual(response.context['object_list'], ['<Students: Валера>'])
        self.assertContains(response, 'Валера')
        self.assertContains(response, 'Пономаренко')
        self.assertContains(response, 'Киев, ул. Артема, 56, кв 11')
        self.assertContains(response, 'sergei.4e')
        self.assertContains(response, 'Курс Python')

    def test_students_view_with_3_students(self):
        create_student(name='Валера', surname='Пономаренко', course=['Python'])
        create_student(name='Сергей', surname='Черненко', course='Java')
        create_student(name='Андрей', surname='Иванов', course='php')
        response = self.client.get(reverse('student_list'))
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Students: Валера>', '<Students: Сергей>'],
                                 ordered=False)
        self.assertEqual(len(response.context['object_list']), 2)

    def test_students_view_with_get_course_id(self):
        create_student(name='Валера', surname='Пономаренко', course=['Python'])
        create_student(name='Сергей', surname='Черненко', course=['Java'])
        create_student(name='Андрей', surname='Иванов', course=['php'])
        c = Client()
        response = c.get('/students/', {'course_id': 3})
        self.assertQuerysetEqual(response.context['object_list'], ['<Students: Андрей>'])

    def test_one_student_view_with_2_courses(self):
        test_student = create_student(name='Вениамин', surname='Аристархович', course=['Python', 'php'])
        response = self.client.get('/student_detail/1/')
        self.assertEqual(response.context["object"], test_student)
        self.assertContains(response, 'Python</a>')
        self.assertContains(response, 'php</a>')
        self.assertContains(response, '<h2>Вениамин Аристархович</h2>')
        self.assertContains(response, '25.03.1986')
        self.assertContains(response, 'Киев, ул. Артема, 56, кв 11')
        self.assertContains(response, 'sergei.4e@gmail.com')
        self.assertContains(response, 'sergei.4e')
        self.assertContains(response, '0446782453')
