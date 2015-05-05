from django.test import TestCase

from django.test import Client
from students.models import Student


students = {
    'student1': {
        'name': 'Ivan',
        'surname': 'Petrov',
        'birth_date': '1981-02-02',
        'email': 'student1@test.com',
        'phone': '12345',
        'address': 'addr1',
        'skype': 'skype1',
    },
    'student2': {
        'name': 'Peter',
        'surname': 'Ivanov',
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

        # checking if surname is present
        self.assertContains(response, "Petrov", status_code=200)
        #print response
        self.assertContains(response, "Ivanov", status_code=200)


class ItemDetailTests(TestCase):

    def test_item_detail(self):
        # create some student items
        create_student(students['student1'])
        create_student(students['student2'])

        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, "Petrov", status_code=200)

        response = client.get('/students/2/')
        self.assertContains(response, "Ivanov", status_code=200)



