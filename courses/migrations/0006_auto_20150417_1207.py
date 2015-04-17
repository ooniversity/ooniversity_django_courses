# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20150411_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(to='coaches.Coach'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(related_name='course_lesson', to='courses.Course'),
            preserve_default=True,
        ),
    ]
