# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Photo (models.Model):
    discription = models.CharField(verbose_name=u'Описание фото', max_length=60, null=True, blank=True)
    photo = models.ImageField(upload_to='static/images/Photos/', verbose_name=u'Фото')

    def __unicode__(self):
        return self.discription
