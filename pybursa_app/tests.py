# ~*~ coding: utf-8 ~*~
from django.test import TestCase
from django.test import Client
from students.models import Student
from courses.models import Course


class Pybursa_appTest(TestCase):
    def test_student_create(self):
        student = Student.objects.create(
            student_last_name = 'Иванов',
            student_name = 'Петя')
        self.assertEqual(Student.objects.all().count(), 1)

    def test_student_list(self):
        student = Student.objects.create(
            student_last_name = 'Иванов',
            student_name = 'Петя')
        client = Client()
        response = client.get('/student_list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['student_list']), 1)

        self.assertQuerysetEqual(response.context['student_list'], ['<Student: Иванов>'])
        self.assertQuerysetEqual(response.context['course_list'], [])

    def test_student_detail(self):
        student = Student.objects.create(
            student_last_name = 'Иванов',
            student_name = 'Петя')
        client = Client()
        response = client.get('/student_list/1/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['student_list'], ['<Student: Иванов>'])
        self.assertQuerysetEqual(response.context['course_list'], [])

class CourseTest(TestCase):
    def test_course_create(self):
        course = Course.objects.create(
            course_name = 'Django',
            course_brief = 'Создание сайтов')
        self.assertEqual(Course.objects.all().count(), 1)
    def test_course_list(self):
        course = Course.objects.create(
            course_name = 'Django',
            course_brief = 'Создание сайтов')
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['course_list']), 1)
        self.assertQuerysetEqual(response.context['course_list'], ['<Course: Django>'])


    def test_course_detail(self):
        course = Course.objects.create(
            course_name = 'Django',
            course_brief = 'Создание сайтов')
        client = Client()

        response = client.get('/course/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(course.course_name, 'Django')
        self.assertQuerysetEqual(response.context['lesson_list'], [])
        self.assertQuerysetEqual(response.context['student_list'], [])

    def test_course_student(self):
        course = Course.objects.create(
            course_name = 'Django',
            course_brief = 'Создание сайтов')
        student = Student.objects.create(
            student_last_name = 'Иванов',
            student_name = 'Петя')
        client = Client()
        student.student_course.id = course.id

        response = client.get('/student_list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['course_list']), 1)
        self.assertEqual(course.course_name, 'Django')
        self.assertQuerysetEqual(response.context['course_list'], ['<Course: Django>'])
        self.assertQuerysetEqual(response.context['student_list'], ['<Student: Иванов>'])
