from django.test import TestCase

from django.test import Client
from courses.models import Course


items = {
    'course1': {
        'title': 'Course1',
        'comment': 'Course1 comment',
        'description': 'course1 description',
    },
    'course2': {
        'title': 'Course2',
        'comment': 'Course2 comment',
        'description': 'course2 description',
    }
}

def create_item(item):
    return Course.objects.create(**item)


def create_items():
    for item in items.keys():
        #print item
        create_item(items[item])


class ItemsListTests(TestCase):

    def test_list_items(self):

        # create some student items
        create_items()
        self.assertEqual(Course.objects.all().count(), 2)

        client = Client()
        response = client.get('/courses/')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Course1", status_code=200)
        #print response
        self.assertContains(response, "Course2", status_code=200)


class ItemDetailTests(TestCase):

    def test_item_detail(self):
        # create some student items
        create_item(items['course1'])
        create_item(items['course2'])

        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, "Course1", status_code=200)

        response = client.get('/courses/2/')
        self.assertContains(response, "Course2", status_code=200)


