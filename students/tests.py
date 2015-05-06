# -*- coding: utf-8 -*-
from django.test import TestCase

from students.models import Student

class StudentsTests(TestCase):

	def test_student_list(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.all().count(), 0)

		student1 = Student.objects.create(
			name = 'Grigoriy', 
			surname = 'Grigoriev',
			birth_date = '1990-02-10',
			email = 'namesurname@ukr,net',
			phone = '0668787678',
			adress = 'Kharkiv',
			skype = 'namesurname'
			)

		response = client.get('/students/')
		self.assertEqual(Student.objects.all().count(), 1)
		self.assertContains(response, 'Grigoriy')


	def test_student_page(self):
		from django.test import Client

		client = Client()
		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

		student1 = Student.objects.create(
			name = 'Grigoriy', 
			surname = 'Grigoriev',
			birth_date = '1990-02-10',
			email = 'namesurname@ukr.net',
			phone = '0668787678',
			adress = 'Kharkiv',
			skype = 'namesurname'
			)

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.all().count(), 1)
		
		self.assertContains(response, 'Grigoriy')
