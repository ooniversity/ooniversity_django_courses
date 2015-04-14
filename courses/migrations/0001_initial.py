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
                ('name', models.CharField(max_length=20, verbose_name=b'Course name')),
                ('info', models.CharField(max_length=200, null=True, verbose_name=b'Short info', blank=True)),
                ('discription', models.TextField(null=True, verbose_name=b'Course discription', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme', models.CharField(max_length=40, verbose_name=b'Theme of lesson')),
                ('discription', models.TextField(null=True, verbose_name=b'Lesson discription', blank=True)),
                ('number', models.PositiveIntegerField(unique=True, verbose_name=b'Number of lesson')),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
