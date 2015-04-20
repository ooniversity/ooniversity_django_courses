# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150412_0003'),
        ('students', '0011_student_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=75)),
                ('package', models.CharField(max_length=32)),
                ('comment', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('courses', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
