# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20150411_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['student_last_name']},
        ),
        migrations.AlterField(
            model_name='student',
            name='student_course',
            field=models.ManyToManyField(to='courses.Course', verbose_name=b'\xd0\x9a\xd1\x83\xd1\x80\xd1\x81\xd1\x8b'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('student_last_name', 'student_name')]),
        ),
    ]
