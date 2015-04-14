# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=100)),
                ('course_brief', models.CharField(max_length=200)),
                ('course_description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson_theme', models.CharField(max_length=100)),
                ('lesson_description', models.TextField()),
                ('lesson_number', models.PositiveIntegerField()),
                ('lesson_course', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
