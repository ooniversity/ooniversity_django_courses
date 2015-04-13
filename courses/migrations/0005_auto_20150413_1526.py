# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0004_auto_20150408_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_assistent',
            field=models.ForeignKey(related_name='assistent_course', verbose_name=b'\xd0\x90\xd1\x81\xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbd\xd1\x82', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='course_coach',
            field=models.ForeignKey(related_name='coach_course', verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb5\xd1\x80', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
