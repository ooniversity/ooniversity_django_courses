import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse

from students.models import Student
from courses.models import Course


class StudentTests(TestCase):
    def test_student_list(self):
        from django.test import Client
        client = Client()

        course = Course.objects.create(
            title="HTML",
            descr_sm="shjkfhjs",
            descr_full="sgdhfgjehsfa"
        )

        student_1 = Student.objects.create(
            name="Joui",
            surname="Summm",
            birthday="1998-12-09",
            email="joui@gmail.com",
            phone_num="+380575432233",
            address="Kyiv, vuluca Engelsa, 234",
            skype="asgdh.hh"
        )
        student_1.courses.add(course)

        student_2 = Student.objects.create(
            name="Lui",
            surname="Myth",
            birthday="1978-02-19",
            email="lui@gmail.com",
            phone_num="+380575432255",
            address="Kyiv, vuluca Engelsa, 234",
            skype="asdf.asd"
        )
        student_2.courses.add(course)

        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 2)
        self.assertContains(response, u'Myth')
        self.assertEqual(student_1.email, 'joui@gmail.com')
        self.assertContains(response, u'asdf.asd')
        self.assertContains(response, u'Summm')
        self.assertEqual(student_2.email, 'lui@gmail.com')
        self.assertContains(response, u'asgdh.hh')
        self.assertContains(response, u'HTML')

    def test_student_detail(self):
        from django.test import Client
        client = Client()

        course = Course.objects.create(
            title="CSS",
            descr_sm="sbf",
            descr_full="zcxvbzzn"
        )

        student_1 = Student.objects.create(
            name="Joui",
            surname="Summm",
            birthday=datetime.date(1987, 2, 15),
            email="asda@gmail.com",
            phone_num="+380575432211",
            address="Kyiv, vuluca Engelsa, 234",
            skype="adad.dhj"
        )
        student_1.courses.add(course)

        response = client.get(reverse(
            'students:student-detail',
            args=(student_1.id,))
        )

        self.assertContains(response, student_1.surname, status_code=200)
        self.assertContains(response, u'Summm')
        self.assertContains(response, u'asda@gmail.com')
        self.assertContains(response, u'adad.dhj')
        self.assertContains(response, u'CSS')
