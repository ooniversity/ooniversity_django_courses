from django.test import TestCase

from django.test import Client
from students.models import Student


students = {
    'student1': {
        'name': 'Stu1',
        'surname': 'Stu1',
        'birth_date': '1981-02-02',
        'email': 'student1@test.com',
        'phone': '12345',
        'address': 'addr1',
        'skype': 'skype1',
    },
    'student2': {
        'name': 'Stu2',
        'surname': 'Stu2',
        'birth_date': '1980-01-02',
        'email': 'student2@test.com',
        'phone': '12345',
        'address': 'addr2',
        'skype': 'skype2',
    }
}

def create_student(student):
    return Student.objects.create(**student)


def create_items():
    for item in students.keys():
        #print item
        create_student(students[item])


class ItemsListTests(TestCase):

    def test_list_items(self):

        # create some student items
        create_items()
        self.assertEqual(Student.objects.all().count(), 2)

        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Stu1", status_code=200)
        #print response
        self.assertContains(response, "Stu2", status_code=200)


