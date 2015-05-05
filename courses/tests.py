# -*- coding: UTF-8 -*-
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from courses.models import Course


class CourseMethodTests(TestCase):

    def test_list_courses(self):
    	client = Client()
    	course1 = Course.objects.create(name = "Course1", 
    		                            short_description = "Interesting course")
        course2 = Course.objects.create(name = "Course2", 
        	                            short_description = "Very interesting course")
        response = client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['courses'].order_by('name'),
            ['<Course: Course1>', '<Course: Course2>']
        )
        
    def test_view_course(self):
    	client = Client()
    	response = client.get('/courses/1/')
    	self.assertEqual(response.status_code, 404)
    	course = Course.objects.create(name = "Course1", 
    		                           short_description = "Interesting course",
    		                           description = "This course suggests to learn a high mathematics")
    	response = client.get('/courses/1/')
    	self.assertEqual(response.status_code, 200)
    	self.assertContains(response, course.name)
    	self.assertContains(response, course.description)
        
