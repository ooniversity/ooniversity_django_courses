# -*- coding: utf-8 -*-


from django.test import TestCase
from courses.models import Course
from django.test import Client


class CourseTests(TestCase):

    # тест Алексея из видео
    def test_course_create_object(self):
        # создание объектов курсов
        course1 = Course.objects.create(
            name='Python/Django',
            short_description=u'Профессиональные Python курсы'
        )
        course2 = Course.objects.create(
            name='',
            short_description=u''
        )
        # проверка что курсы создались
        self.assertEqual(Course.objects.all().count(), 2)

    # тест списка курсов
    def test_courses_list(self):
        # запуск проекта
        client = Client()
        # переходим на страницу списка курсов
        response = client.get('/')
        # проверка что страничка работает
        self.assertEqual(response.status_code, 200)
        # проверка что б.д. пуста
        self.assertEqual(Course.objects.all().count(), 0)
        # создадим курс
        course1 = Course.objects.create(
            name='Python/Django',
            short_description=u'Профессиональные Python курсы'
        )
        # проверим что курс создался
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Профессиональные Python курсы')   # почему-то 'Python/Django' не сработало
        self.assertEqual(Course.objects.all().count(), 1)

    # тест создания курса
    def test_course_create(self):
        # запуск сервера
        client = Client()
        # проверяем что курса нет
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        # создаем курс
        course1 = Course.objects.create(
            name='Python/Django',
            short_description=u'Профессиональные Python курсы'
        )
        # проверка что курс создался
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python/Django")