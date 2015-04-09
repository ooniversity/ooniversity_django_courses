# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150409_0610'),
        ('students', '0007_remove_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course', verbose_name='\u041a\u0443\u0440\u0441\u044b'),
            preserve_default=True,
        ),
    ]
