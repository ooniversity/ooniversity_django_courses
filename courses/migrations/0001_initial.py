# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('assistant', models.ForeignKey(related_name='assistants', blank=True, to='coaches.Coach', null=True)),
                ('trainer', models.ForeignKey(related_name='trainers', blank=True, to='coaches.Coach', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('num', models.PositiveIntegerField()),
                ('course', models.ForeignKey(related_name='lessons', to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
