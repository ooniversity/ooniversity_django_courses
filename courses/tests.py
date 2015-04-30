# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from courses.models import Course, Lesson


class CourseTest(TestCase):

    def test_pages(self):
        client = Client()
        #Проверка на случай, когда ни один курс не создан
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'нет активных курсов')
        #Создаем два курса
        course1 = Course.objects.create(name='Python', info='Web development with Python')
        course2 = Course.objects.create(name='Django', info='Web development with Django')
        #Проверяем, что страничка отвечает
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        #Проверяем, что количество созданных курсов соответсвует количеству курсов на страничке
        self.assertEqual(Course.objects.all().count(), 2)

        #Проверяем, что содержимое курсов выводится правильно
        for contextData in Course.objects.all():
            self.assertContains(response, contextData.name)
            self.assertContains(response, contextData.info)


#Проверка странички конкретного курса CourseDetail
class CourseDetailTest(TestCase):

    def test_course_detail(self):
        courseNumber = 1 #Номер вызываемого курса
        client = Client()
        response = client.get(reverse('courses:course', args=(courseNumber,)))
        #Проверка обращения к несуществующей странице
        self.assertEqual(response.status_code, 404)

        #Создаю курс и нескольно уроков
        course1 = Course.objects.create(name='Python', info='Web development with Python',
                                        discription=u'Python - это хороший язык. Успехов в изучении!')
        #Создаем много студентов
        for i in xrange(10):
            newLesson = Lesson.objects.create(theme=u'Тема {}'.format(i+1),
                                               discription='Описание урока {}'.format(i+1),
                                               course=course1,
                                               number=i+1,)

        #Проверка, что страница отвечает и курс выводится правильно
        response = client.get(reverse('courses:course', args=(courseNumber,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course1.name)
        self.assertContains(response, course1.discription)
        #Проверка, что все уроки курса выводятся
        for lesson in course1.lesson_set.all():
            self.assertContains(response, lesson.theme)
            self.assertContains(response, lesson.discription)

