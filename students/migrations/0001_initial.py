# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_name', models.CharField(max_length=20)),
                ('student_last_name', models.CharField(max_length=30)),
                ('student_birth', models.DateField(null=True, blank=True)),
                ('student_email', models.EmailField(max_length=75)),
                ('student_phone', models.CharField(max_length=20)),
                ('student_addr', models.CharField(max_length=50)),
                ('student_skype', models.CharField(max_length=50)),
                ('student_course', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
