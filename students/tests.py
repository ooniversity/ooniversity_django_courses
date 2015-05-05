# -*- coding: UTF-8 -*-
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from students.models import Student


class StudentMethodTests(TestCase):

    def test_list_students(self):
    	client = Client()
    	student1 = Student.objects.create(name = "Ivan", 
    		                              surname = "Ivanov",
    		                              date_birthday = '1995-04-02')
        student2 = Student.objects.create(name = "Petr", 
        	                              surname = "Petrov",
        	                              date_birthday = '1995-04-02')
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['student_list'].order_by('name'),
            ['<Student: Ivanov>', '<Student: Petrov>']
        )
        
    def test_view_student(self):
    	client = Client()
    	response = client.get('/students/1/')
    	self.assertEqual(response.status_code, 404)
    	student = Student.objects.create(name = "Petr", 
        	                             surname = "Petrov",
        	                             date_birthday = '1995-04-02')
    	response = client.get('/students/1/')
    	self.assertEqual(response.status_code, 200)
    	self.assertContains(response, student.name)
    	self.assertContains(response, student.surname)
        


