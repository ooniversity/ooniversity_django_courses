from django.test import TestCase
from students.models import Student
from courses.models import Course, Lesson
from coaches.models import Coach
from django.core.urlresolvers import reverse
import datetime
#from coaches import urls# as test_urls
#from pybursa import urls# as test_urls
#import pybursa.urls
#from django.conf.urls import patterns
#from coaches.views import *
from django.contrib.auth.models import User

def lesson_course(topic):
    return Lesson.objects.create(
        topic=topic,
        description='LessonDescription',
        index=1)

class CourseTests(TestCase):
    """
    #urls = 'coaches.test_urls'
    #urls = 'coaches.urls'
    urls = 'pybursa.urls'
    #urls += patterns('',
    #    (r'^coaches/(?P<pk>\d+)/$', coach_detail ),
    #)

    def setUp(self):
        super(CourseTests, self).setUp()
        self.original_urls = pybursa.urls.urlpatterns
        pybursa.urls.urlpatterns += patterns(
            '',
            (r'^coaches/(?P<pk>\d+)/$', coach_detail),
        )    


    def tearDown(self):
        super(CourseTests, self).tearDown()
        pybursa.urls.urlpatterns = self.original_urls
    """

    def test_course_list(self): 
        from django.test import Client
        client = Client()

        """
        course1 = create_course('CourseName1')
        course1.save()#????
        course2 = create_course('CourseName2')
        course2.save()#????
        """

        course1 = Course.objects.create(
            name = 'CourseName1',
            short_description='CourseShortDescr1',
            description='CourseDescription1',
            ) 
        #course1.save()#????

        course2 = Course.objects.create(
            name = 'CourseName2',
            short_description='CourseShortDescr2',
            description='CourseDescription2',
            ) 
        #course2.save()#????

        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(Course.objects.all().count(), 2)

        for item in Course.objects.all():
            self.assertContains(response, item.name.upper())

        for item in Course.objects.all():
            self.assertContains(response, item.short_description)
        #no full course desctiption at the template!

        #self.assertTrue('courses' in response.context)# no need!
        #self.assertEqual(course1.name, 'CourseName1')#????? no need!
        #self.assertEqual(course2.name, 'CourseName2')#????? no need!
        #self.assertContains(response, 'CourseShortDescr1')#already checked
        #self.assertContains(response, 'CourseShortDescr2')#already checked

        self.assertEqual(response.context['courses'][0].name, course1.name) 
        self.assertEqual(response.context['courses'][1].name, course2.name) 

        self.assertEqual(response.context['courses'][0].short_description, course1.short_description) 
        self.assertEqual(response.context['courses'][1].short_description, course2.short_description) 
        

    def test_course_detail(self):
        from django.test import Client
        client = Client()

        response = client.get(reverse(
                                'courses:course', 
                                args=(1,)))
        self.assertEqual(response.status_code, 404) 

        #USER model in tests: 
        #http://stackoverflow.com/questions/2840467/problems-using-user-model-in-django-unit-tests

        self.u1 = User.objects.create(username='UserName1')
        #self.u1.save()#????
        self.u2 = User.objects.create(username='UserName2')
        #self.u2.save()#????

        coach1 = Coach.objects.create(
            user=self.u1,
            #user.get_full_name()
            birth_date=datetime.date(1982, 2, 13),
            gender='M',
            phone='332-555-664',
            address='address1',
            scype='scype1',
            description='coach1 description')
        #coach1.save()#????

        coach2 = Coach.objects.create(
            user=self.u2,
            #user='UserName2', #user = models.OneToOneField(User, null=True, blank=True)
            birth_date=datetime.date(1982, 1, 13),
            gender='F',
            phone='332-555-665',
            address='address2',
            scype='scype2',
            description='coach2 description')
        #coach2.save()#????

        course1 = coach1.rel_trainers.create(
            name = 'CourseName1',
            short_description='CourseShortDescr',
            description='CourseDescription',
            #trainer = coach1,
            #assistant = coach2
            ) 

        coach2.rel_assistants.add(course1)

        """
        course1 = Course.objects.create(
            name = 'CourseName1',
            short_description='CourseShortDescr',
            description='CourseDescription',
            #trainer = coach1,
            #assistant = coach2
            ) 
        """
        #course1.trainer.rel_trainers.add(coach1)#???????????????
        #course1.assistant.rel_assistants.add(coach2)#???????????????        

	"""
	class Article(models.Model):
	    headline = models.CharField(max_length=100)
	    pub_date = models.DateField()
	    reporter = models.ForeignKey(Reporter)

	r = Reporter(first_name='John', last_name='Smith', email='john@example.com')
	new_article = r.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29))

	new_article2 = Article(headline="Paul's story", pub_date=date(2006, 1, 17))
	r.article_set.add(new_article2)

	"""
        #course1.save()#????

        lesson1 = Lesson.objects.create(
            description='lesson1Description',
            course=course1,
            index = 1)
        #lesson1.save()#????

        lesson2 = Lesson.objects.create(
            description='lesson2Description',
            course=course1,
            index = 2)
        #lesson2.save()#????


        """
        response = client.get(reverse(
                                 'courses:course', 
                                 args=(course1.pk,)))#IT ALSO WORKS
        """
        response = client.get(reverse(
                                 'courses:course', 
                                 args=(Course.objects.get().pk,)))#IT ALSO WORKS

        self.assertEqual(response.status_code, 200)    
        self.assertTrue('object' in response.context) #does it check course name??? (see course model self)

        self.assertContains(response, course1.name)
        self.assertContains(response, course1.description)
        #here - too short to test truncation;
        #in template truncated to 250 symbols: {{course.description|truncatechars:250}}

        self.assertEqual(response.context['object'].pk, course1.pk)   
        self.assertEqual(response.context['object'].name, 
                         course1.name)

        self.assertEqual(Course.objects.all().count(), 1)
        self.assertEqual(Coach.objects.all().count(), 2)
        self.assertEqual(Lesson.objects.all().count(), 2)

        for item in Lesson.objects.all():
            self.assertContains(response, item.description)

        for item in User.objects.all():
            self.assertContains(response, item.get_full_name())
            #/upper() is not necessary/

        for item in Coach.objects.all():
            self.assertContains(response, item.description)

        self.assertEqual(response.context['object'].trainer.user, self.u1)
        self.assertEqual(response.context['object'].assistant.user, self.u2)

        #self.assertContains(response, lesson1)#it works but already checked
        #self.assertContains(response, lesson2)#it works but already checked
        #self.assertContains(response, self.u1.get_full_name())#it works but already checked
        #self.assertContains(response, self.u2.get_full_name())#it works but already checked
        #self.assertContains(response, course1.trainer) #doesn't work
        #self.assertContains(response, course1.assistant) #doesn't work
