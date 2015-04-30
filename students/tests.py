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
    #check ListView when no student exists
    #def test_students_empty_list(self): 

    #check ListView when students exist:
    def test_students_list(self): 
        from django.test import Client
        client = Client()
        #create_student('StudentSurname1')

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
        #print response.context['object_list'] #no need to print
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(Student.objects.all().count(), 2)
        #context testing:
        #https://docs.djangoproject.com/en/1.7/intro/tutorial05/#testing-our-new-view
        #'object_list' instead of 'student_list' is also possible

        """       
        self.assertQuerysetEqual(
            response.context['student_list'],
            #['<Student: StudentSurname1>']#can we parametrize???
            ['<Student: StudentSurname1>', '<Student: StudentSurname2>']
        )
        """

        """
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
        """
        #https://docs.djangoproject.com/en/1.7/topics/testing/tools/#django.test.Response.context
        #http://django-testing-docs.readthedocs.org/en/latest/views.html
        """
        self.assertEqual([student.pk for student in response.context['student_list']], [1])
        """
        self.assertTrue('student_list' in response.context)
        self.assertEqual(student1.email, 'email1@email.email')#?????
        self.assertEqual(student2.email, 'email2@email.email')#?????

        self.assertContains(response, 'CourseName1')
        self.assertContains(response, 'StudentName1')
        self.assertContains(response, 'StudentName2')
        self.assertContains(response, 'STUDENTSURNAME1')#upper!
        self.assertContains(response, 'STUDENTSURNAME2')#upper!
        self.assertContains(response, 'address1')
        self.assertContains(response, 'address2')
        self.assertContains(response, 'scype1')
        self.assertContains(response, 'scype2')

        self.assertEqual(response.context['student_list'][0].name, 
                         'StudentName1') 
        self.assertEqual(response.context['student_list'][1].name, 
                         'StudentName2') 
        
        self.assertEqual(response.context['student_list'][0].name, 
                         student1.name) #???????????????
        self.assertEqual(response.context['student_list'][1].name, 
                         student2.name) #???????????????
        
        #self.assertEqual([student.courses.count() for student in response.context['student_list']], [1])
        #self.assertTrue(not student.courses for student in response.context['student_list'])#?????? not student.courses ALSO WORKS!!!
        #self.assertTrue(students)#AssertionError: [] is not true
        #self.assertTrue(students.count())#AssertionError: 0 is not true
        #self.assertEqual(student.courses, 1) #AssertionError: <django.db.models.fields.related.ManyRelatedManager object at 0x7ffe8094c5d0> != 1
        #self.assertEqual((student.courses for student in response.context['student_list']), 1) #AssertionError: <generator object <genexpr> at 0x7f40f8588370> != 1

#CHECK IF STUDENT OBJECT CAN CONTAIN SEVERAL COURSES!!
#need it really??? M2M!!! not evident?!


    #https://docs.djangoproject.com/en/1.7/intro/tutorial05/#testing-the-detailview
    def test_student_detail(self):
        from django.test import Client
        client = Client()

        #response = client.get('/students/1/')
        response = client.get(reverse(
                                'students:student_one', 
                                args=(1,)))
        self.assertEqual(response.status_code, 404) 

        student1 = Student.objects.create(
            name='StudentName1', 
            surname='StudentSurname1',
            birth_date='1988-01-01',#'YYYY-MM-DD'
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
                                 args=(student1.pk,)))#???????????????
        #response = client.get(reverse(
        #                        'students:student_one', 
        #                        args=(1,)))
        #print response.context['object'] #no need to print
        self.assertEqual(response.status_code, 200)    
        self.assertTrue('student' in response.context) 
        self.assertContains(response, "StudentName1")
        #context testing:
        #http://toastdriven.com/blog/2011/apr/10/guide-to-testing-in-django/
        #self.assertEqual(response.context['student'].pk, 1)   
        self.assertEqual(response.context['student'].pk, student1.pk)   
        #'object' instead of 'student' is also possible
        self.assertEqual(response.context['student'].name, 
                         'StudentName1')#to parametrize!
        self.assertEqual(response.context['student'].surname,
                         student1.surname) 
        self.assertContains(response, 'StudentName1')
        self.assertContains(response, '1988, January 1')
        #self.assertContains(response, '1988-01-01')
        #self.assertContains(response, datetime.date(1988, 1, 1))
        #AssertionError: datetime.date(1988, 1, 1) != '1988-01-01'
        #self.assertEqual(response.context['student'].birth_date, 
                         #student1.birth_date)
        """
        self.assertEqual(response.context['student'].email, 
                         student1.email) 
        self.assertEqual(response.context['student'].phone,
                         student1.phone) 
        self.assertEqual(response.context['student'].address,
                         student1.address)  
        self.assertEqual(response.context['student'].scype, 
                         student1.scype) 
        """
        self.assertEqual(response.context['student'].name, 
                         'StudentName1') 
        self.assertEqual(response.context['student'].surname,
                         'StudentSurname1') 
        self.assertEqual(response.context['student'].email, 
                         'email1@email.email') 
        self.assertEqual(response.context['student'].phone,
                         '333-555-666') 
        self.assertEqual(response.context['student'].address,
                         'address1')  
        self.assertEqual(response.context['student'].scype, 
                         'scype1') 

        self.assertContains(response, 'CourseName1')
        self.assertContains(response, 'CourseName2')

        #http://toastdriven.com/blog/2011/apr/10/guide-to-testing-in-django/
        courses=student1.courses.all()
        self.assertEqual(courses[0].pk, course1.pk) #???
        self.assertEqual(courses[1].pk, course2.pk) #???
        #self.assertEqual(courses[0].pk, 1)
        self.assertEqual(courses.count(), 2)
