# -*- coding: utf-8 -*-
import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client

from courses.models import Course
from students.models import Student


#Проверка страничек со списками студентов StudentList
class StudentListTest(TestCase):
    #Тест:
    #страницы со спискам студентов работают (код ответа 200) и содержит информацию из заранее созданых объектов
    def test_students_list(self):
        client = Client()
        response = client.get(reverse('students:student-list'))
        self.assertEqual(response.status_code, 200)
        #Проверка, когда ни один студент не зарегистрировался
        self.assertContains(response, 'ни один студент пока не зарегистрирован')

        #Создаем много студентов
        for i in xrange(1000):
            newStudent = Student.objects.create(name='Victor', surname='Ivanov',
                                              date_of_birth=datetime.date(1999, 01, 05),)

        response = client.get(reverse('students:student-list'))
        self.assertEqual(response.status_code, 200)
        #Проверка количества студентов
        self.assertEqual(Student.objects.all().count(), 1000)

        # Проверка, что все студенты выводятся с правильными именами
        for newStudent in Student.objects.all():
            self.assertContains(response, '{} {}'.format(newStudent.surname.upper(), newStudent.name.upper()))

    #Тестирования странички студентов конкретного курса
    def test_students_list_course(self):
        courseNumber = 2 #задаем номер курса для тестирования
        client = Client()
        response = client.get(reverse('students:student-list') + '?course_id={}'.format(courseNumber))
        self.assertEqual(response.status_code, 200)
        #Проверка, когда ни один студент не зарегистрировался
        self.assertContains(response, 'ни один студент пока не зарегистрирован')
        #Создаем два курса
        course1 = Course.objects.create(name='Python', info='Web development with Python')
        course2 = Course.objects.create(name='Django', info='Web development with Django')

        #Создаем 10 студентов и распределяем их на курсы
        for i in xrange(5):
            newStudent = Student.objects.create(name='Victor', surname='Ivanov',
                                              date_of_birth=datetime.date(1999, 01, 05),
                                              email='nb@gmail.com', phone=03,)
            newStudent.courses.add(course1, course2)
            newStudent.save()

            newStudent = Student.objects.create(name='Victor', surname='Lunev',
                                              date_of_birth=datetime.date(1990, 05, 05),
                                              email='nb@gmail.com', phone=02,)
            newStudent.courses.add(course1)
            newStudent.save()

        response = client.get(reverse('students:student-list') + '?course_id={}'.format(courseNumber))
        self.assertEqual(response.status_code, 200)
        #Проверка количества студентов конкретного курса
        self.assertEqual(Student.objects.filter(courses__id=courseNumber).count(), 5)

        # Проверка, что все студенты конкретного курса выводятся с правильными именами
        for newStudent in Student.objects.filter(courses__id=courseNumber):
            self.assertContains(response, '{} {}'.format(newStudent.surname.upper(), newStudent.name.upper()))


#Проверка странички конкретного студента StudentDetail
class StudentDetailTest(TestCase):

    def test_student_detail(self):
        studentNumber = 1 #Номер вызываемого студента
        client = Client()
        response = client.get(reverse('students:student-detail', args=(studentNumber,)))
        #Проверка обращения к несуществующей странице
        self.assertEqual(response.status_code, 404)

        #Создаю два курса, студента и записываю его на эти курсы
        course1 = Course.objects.create(name='Python', info='Web development with Python')
        course2 = Course.objects.create(name='Django', info='Web development with Django')
        studentData = [u'Алена', u'Твердохлеб', datetime.date(1987, 05, 05), 'nb@gmail.com', 02,
                        u'Украина, п.Краснокутск, ул. Ленина 382', 'alenushka', course1.name, course2.name]
        newStudent = Student.objects.create(name=studentData[0], surname=studentData[1],
                                            date_of_birth=studentData[2],
                                            email=studentData[3], phone=studentData[4],
                                            address=studentData[5],
                                            skype=studentData[6], )
        newStudent.courses.add(course1, course2)
        newStudent.save()
        #Проверка, что страница отвечает и студент выводится правильно
        response = client.get(reverse('students:student-detail', args=(studentNumber,)))
        self.assertEqual(response.status_code, 200)
        for content in studentData:
            if content == datetime.date(1987, 05, 05):
                content = content.strftime("%d %B %Y")
            self.assertContains(response, content)
