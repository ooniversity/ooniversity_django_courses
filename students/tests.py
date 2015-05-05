from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from courses.models import Course
from students.models import Student
import datetime

class StudentListTest(TestCase):

	def test_students_list(self):
		client = Client()
		response = client.get(reverse('students:student_list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'No students here')

		for i in xrange(50):
			nStudent = Student.objects.create(name='Mike', surname='Bisket',
												birthday=datetime.date(1999, 01, 05),)

		response = client.get(reverse('students:student_list'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.all().count(), 50)

		for nStudent in Student.objects.all():
			self.assertContains(response, '{}'.format(nStudent.name))

	def test_st_list_course(self):
		courseNumber = 1
		client = Client()
		response = client.get(reverse('students:student_list') + '?course_id={}'.format(courseNumber))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'No students here')

		course1 = Course.objects.create(name='Eng 101', brief='English 101')
		course2 = Course.objects.create(name='Eng 102', brief='English 102')

		for i in xrange(5):
			nStudent = Student.objects.create(name='Mike', surname='Bisket',
											  birthday=datetime.date(1999, 01, 05),
											  email='same@yahoo.com', cell=2535674746,)
			nStudent.courses.add(course1, course2)
			nStudent.save()

		response = client.get(reverse('students:student_list') + '?course_id={}'.format(courseNumber))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.filter(courses__id=courseNumber).count(), 5)

		for nStudent in Student.objects.filter(courses__id=courseNumber):
			self.assertContains(response, '{}'.format(nStudent.name))

class StudentDetailTest(TestCase):

	def test_student_detail(self):
		studentNumber = 1
		client = Client()
		response = client.get(reverse('students:student_detail', args=(studentNumber,)))
		self.assertEqual(response.status_code, 404)

		course1 = Course.objects.create(name='Eng 101', brief='English 101')
		course2 = Course.objects.create(name='Eng 102', brief='English 102')
		
		nStudent = Student.objects.create(name='Mike', surname='Bisket',
										birthday=datetime.date(2000, 01, 01),
										email='same@yahoo.com', cell=2535674746,)
		nStudent.courses.add(course1, course2)
		nStudent.save()

		response = client.get(reverse('students:student_detail', args=(studentNumber,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '{}'.format(nStudent.name.upper()))