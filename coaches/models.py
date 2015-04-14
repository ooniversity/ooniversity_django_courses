# ~*~ coding: utf-8 ~*~

from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    MAN = '1'
    WOMAN = '2'
    CHOICES = (
        (MAN, 'муж'),
        (WOMAN, 'жен'),
    )
    coach_user = models.OneToOneField(User, verbose_name="Тренер", related_name='c_user')
    coach_birth = models.DateField("Дата рождения",blank=True, null=True)
    coach_sex = models.CharField("Пол", choices=CHOICES, default=MAN, max_length=6)
    coach_phone = models.CharField("Телефон",max_length=20,blank=True, null=True)
    coach_addr = models.CharField("Почтовый адрес",max_length=50,blank=True, null=True)
    coach_skype = models.CharField("Логин Skype",max_length=50,blank=True, null=True)
    coach_description = models.TextField("Описание",blank=True, null=True)
    def __unicode__(self):
        return self.coach_description


