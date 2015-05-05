from django.test import TestCase
from students.models import Student
from courses.models import Course
from django.core.urlresolvers import reverse
import datetime

def create_course(name):
    return Course.objects.create(
        name=name,
        short_description='CourseShortDescr',
        description='CourseDescription')  

class StudentTests(TestCase):
    def test_students_list(self): 
        from django.test import Client
        client = Client()

        student1 = Student.objects.create(
            name='StudentName1', 
            surname='StudentSurname1',
            birth_date='1988-01-01',#'YYYY-MM-DD'
            email='email1@email.email',
            phone='333-555-666',
            address='address1',
            scype='scype1')

        student2 = Student.objects.create(
            name='StudentName2', 
            surname='StudentSurname2',
            birth_date=datetime.date(1982, 1, 13),
            email='email2@email.email',
            phone='332-555-666',
            address='address2',
            scype='scype2')

        course1 = create_course('CourseName1')
        student1.courses.add(course1)
        student2.courses.add(course1)

        response = client.get(reverse('students:students'))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(Student.objects.all().count(), 2)
 
        self.assertTrue('student_list' in response.context)

        for item in Student.objects.all():
            self.assertContains(response, item.surname.upper())

        for item in Student.objects.all():
            self.assertContains(response, item.name)

        for item in Student.objects.all():
            self.assertContains(response, item.address)

        for item in Student.objects.all():
            self.assertContains(response, item.scype)

        self.assertEqual(response.context['student_list'][0], 
                         student1) 
        self.assertEqual(response.context['student_list'][1], 
                         student2) 

        #additional checks:
        self.assertEqual(student1.email, 'email1@email.email')
        self.assertEqual(student2.email, 'email2@email.email')

        self.assertContains(response, 'CourseName1')
        self.assertEqual(response.context['student_list'][0].courses.all()[0].name, course1.name) 
        self.assertEqual(response.context['student_list'][1].courses.all()[0].name, course1.name) 
       

    def test_student_detail(self):
        from django.test import Client
        client = Client()

        response = client.get(reverse(
                                'students:student_one', 
                                args=(1,)))
        self.assertEqual(response.status_code, 404) 

        student1 = Student.objects.create(
            name='StudentName1', 
            surname='StudentSurname1',
            birth_date='1988-01-11',#'YYYY-MM-DD'
            email='email1@email.email',
            phone='333-555-666',
            address='address1',
            scype='scype1')

        course1 = create_course('CourseName1')
        course2 = create_course('CourseName2')
        student1.courses.add(course1)
        student1.courses.add(course2)
        response = client.get(reverse(
                                 'students:student_one', 
                                 args=(student1.pk,)))
        self.assertEqual(response.status_code, 200)    
        self.assertTrue('student' in response.context) 
        self.assertContains(response, "StudentName1")  
        self.assertEqual(response.context['student'].pk, student1.pk)   
        #'object' instead of 'student' is also possible
        self.assertEqual(response.context['student'].name, 
                         'StudentName1')#we can parametrize!
        self.assertEqual(response.context['student'].surname,
                         student1.surname) 
        self.assertContains(response, student1.name)
        self.assertContains(response, student1.surname.upper())
        self.assertContains(response, '1988, January 11')
        self.assertContains(response, student1.email)
        self.assertContains(response, student1.phone)
        self.assertContains(response, student1.address)
        self.assertContains(response, student1.scype)

        self.assertEqual(response.context['student'].email, 
                         student1.email) 
        self.assertEqual(response.context['student'].phone,
                         student1.phone) 
        self.assertEqual(response.context['student'].address,
                         student1.address)  
        self.assertEqual(response.context['student'].scype, 
                         student1.scype)   

        self.assertContains(response, 'CourseName1')
        self.assertContains(response, 'CourseName2')
        self.assertEqual(response.context['student'].courses.all()[0].name, course1.name) 
        self.assertEqual(response.context['student'].courses.all()[1].name, course2.name) 
        courses=student1.courses.all()
        self.assertEqual(courses.count(), 2)
        self.assertEqual(courses[0].pk, course1.pk)
        self.assertEqual(courses[1].pk, course2.pk)
