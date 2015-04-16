from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    #user = models.OneToOneField(User)
    user = models.OneToOneField(User, null=True, blank=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=(('1', 'M'),('2', 'F'),))
    phone = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    scype = models.CharField(max_length = 255)
    description = models.TextField()

    def __unicode__(self):
        return '%s' % (self.user) #string!

    def user_name(self):
    #http://stackoverflow.com/questions/3409970/django-admin-how-to-display-fields-from-two-different-models-in-same-view
        if self.user:
            return u'%s %s' % (self.user.last_name, self.user.first_name)
        else:
            return 'no user\'s name defined'

    user_name.short_description = 'Name'
    #user_name.allow_tags = True

    def user_email(self):
        if self.user:
            return self.user.email
        else:
            return 'no user\'s email defined'
    user_email.short_description = 'Email'
    #user_email.allow_tags = True

    class Meta:
        verbose_name_plural = "coaches"

