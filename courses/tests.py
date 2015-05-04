# -*- coding: utf_8 -*-
from django.test import TestCase, Client
from courses.models import Courses, Lesson


def create_course(name):
    course = Courses.objects.create(name=name,
                                    description='Короткое описание курса %s' % name,
                                    text='Это длинное описание курса, описание курса %s' % name)
    return course


def create_lesson(thema, course):
    lesson = Lesson.objects.create(thema=thema,
                                   text='Короткое описание урока %s' % thema,
                                   course=course,
                                   num=33)
    return lesson


class StudentsViewTests(TestCase):

    def test_courses_view_with_no_course(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'На данный момент нет активных курсов')
        self.assertQuerysetEqual(response.context['cour'], [])

    def test_courses_view_with_one_courses(self):
        create_course(name='Python')
        response = self.client.get('/')
        self.assertQuerysetEqual(response.context['cour'], ['<Courses: Python>'])
        self.assertContains(response, "<a href='/courses/1/'>Python</a>")
        self.assertContains(response, 'Короткое описание курса Python')
        self.assertContains(response, 'Изменить</a>')
        self.assertContains(response, 'Удалить</a>')

    def test_courses_view_with_3_courses(self):
        create_course(name='Python')
        create_course(name='Java')
        create_course(name='php')
        response = self.client.get('/')
        self.assertQuerysetEqual(response.context['cour'],
                                 ['<Courses: Python>', '<Courses: Java>', '<Courses: php>'],
                                 ordered=False)

    def test_one_course_view_with_2_lessons(self):
        course = create_course(name='Python')
        create_lesson(thema='Первый урок', course=course)
        create_lesson(thema='Второй урок', course=course)
        response = self.client.get('/courses/1/')
        if not course.trener or not course.assistant:
            self.assertContains(response, '<h4>Преподаватель и Ассистент еще не назначены на данный курс</h4>')
        else:
            self.assertContains(response, course.trener.user.first_name)
            self.assertContains(response, course.assistant.user.first_name)
        self.assertEqual(response.context["object"], course)
        self.assertQuerysetEqual(response.context["lessons"],
                                 ['<Lesson: Первый урок>', '<Lesson: Второй урок>'],
                                 ordered=False)
        self.assertContains(response, 'Python')
        self.assertContains(response, 'Это длинное описание курса, описание курса Python')
